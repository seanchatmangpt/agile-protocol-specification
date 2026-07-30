use crate::autonomics;
use crate::broker::{self, ActuationIntent, ActuationReceipt};
use crate::ledger::ReceiptLedger;
use crate::model::{
    A2A_PROTOCOL_VERSION, A2aArtifact, A2aMessage, A2aPart, A2aTask, A2aTaskState,
    EnterpriseConfig, EnterpriseScale, EnterpriseTopology, Event, MCP_PROTOCOL_VERSION, Metrics,
    ProtocolProfile, ScenarioConfig, ShockKind, SimulationReport, Standing,
};
use serde_json::json;
use sha2::{Digest, Sha256};
use std::collections::BTreeMap;

#[derive(Debug, Clone)]
pub struct EnterpriseEngine {
    pub config: EnterpriseConfig,
    pub scenario: ScenarioConfig,
    pub scale: EnterpriseScale,
    pub topology: EnterpriseTopology,
    pub metrics: Metrics,
    pub ledger: ReceiptLedger,
    tasks: BTreeMap<String, A2aTask>,
    task_counter: u64,
    applied_actuations: usize,
    refused_actuations: usize,
}

impl EnterpriseEngine {
    pub fn new(config: EnterpriseConfig, scenario: ScenarioConfig) -> Result<Self, String> {
        config.validate()?;
        scenario.validate()?;
        let scale = config.scale();
        let topology = config.topology();
        if topology.scale() != scale {
            return Err("generated topology does not match configured scale".to_string());
        }
        Ok(Self {
            scale,
            topology,
            metrics: Metrics::from(&scenario.initial),
            config,
            scenario,
            ledger: ReceiptLedger::new(),
            tasks: BTreeMap::new(),
            task_counter: 0,
            applied_actuations: 0,
            refused_actuations: 0,
        })
    }

    pub fn emit(
        &mut self,
        phase: impl Into<String>,
        kind: impl Into<String>,
        subject: impl Into<String>,
        detail: BTreeMap<String, String>,
    ) -> String {
        self.ledger.append(Event::new(phase, kind, subject, detail))
    }

    pub fn invoke_mcp_action(&mut self, intent: ActuationIntent) -> ActuationReceipt {
        let mut detail = BTreeMap::new();
        detail.insert(
            "protocol_version".to_string(),
            MCP_PROTOCOL_VERSION.to_string(),
        );
        detail.insert("tool".to_string(), intent.action.clone());
        detail.insert("caller".to_string(), intent.requested_by.clone());
        detail.insert("authority".to_string(), intent.authority.clone());
        self.emit("protocol", "mcp.tools/call", intent.target.clone(), detail);
        let receipt = broker::submit(&self.config, &mut self.metrics, &mut self.ledger, intent);
        if receipt.decision == "APPLIED" {
            self.applied_actuations += 1;
        } else {
            self.refused_actuations += 1;
        }
        receipt
    }

    pub fn submit_a2a_task(&mut self, agent: &str, skill: &str, text: &str) -> A2aTask {
        self.task_counter += 1;
        let task_counter = self.task_counter;
        let task_id = format!("a2a-task-{task_counter:06}");
        let scenario_name = &self.scenario.name;
        let context_id = format!("{scenario_name}:pi-simulation");
        let message = A2aMessage {
            role: "user".to_string(),
            parts: vec![A2aPart {
                kind: "text".to_string(),
                text: Some(text.to_string()),
                data: None,
            }],
        };
        let mut task = A2aTask {
            id: task_id.clone(),
            context_id,
            agent: agent.to_string(),
            skill: skill.to_string(),
            state: A2aTaskState::Submitted,
            history: vec![message],
            artifacts: Vec::new(),
            refusal: None,
        };
        let mut submitted = BTreeMap::new();
        submitted.insert(
            "protocol_version".to_string(),
            A2A_PROTOCOL_VERSION.to_string(),
        );
        submitted.insert("agent".to_string(), agent.to_string());
        submitted.insert("skill".to_string(), skill.to_string());
        self.emit("protocol", "a2a.message/send", task_id.clone(), submitted);
        task.state = A2aTaskState::Working;

        match skill {
            "plan-pi" => {
                let data = json!({
                    "portfolios": self.scale.portfolios,
                    "valueStreams": self.scale.value_streams,
                    "solutionTrains": self.scale.solution_trains,
                    "arts": self.scale.arts,
                    "teams": self.scale.teams,
                    "topologyDigest": topology_digest(&self.topology),
                    "activeFeatures": self.metrics.active_features,
                    "blockedFeatures": self.metrics.blocked_features,
                    "guardrails": {
                        "portfolioWipLimit": self.config.portfolio_wip_limit,
                        "architectureEnablerFloorPct": self.config.architecture_enabler_floor_pct,
                        "complianceRiskTolerance": self.config.compliance_risk_tolerance,
                        "autonomics": &self.config.autonomics
                    }
                });
                task.artifacts.push(artifact(
                    &task_id,
                    "pi-plan",
                    "Bounded PI plan across the simulated enterprise topology",
                    data,
                ));
                task.state = A2aTaskState::Completed;
            }
            "resolve-dependency" => {
                let mut parameters = BTreeMap::new();
                parameters.insert("delta_pct".to_string(), "3".to_string());
                let receipt = self.invoke_mcp_action(ActuationIntent {
                    id: format!("{task_id}-rebalance"),
                    action: "safe.capacity.rebalance".to_string(),
                    target: "solution-train-capacity".to_string(),
                    requested_by: format!("a2a:{agent}"),
                    authority: "release-train-engineer".to_string(),
                    parameters,
                });
                task.artifacts.push(artifact(
                    &task_id,
                    "dependency-resolution-receipt",
                    "MCP-backed capacity rebalance result",
                    serde_json::to_value(receipt).expect("receipt serialization must succeed"),
                ));
                task.state = A2aTaskState::Completed;
            }
            "evaluate-release" => {
                let receipt = self.invoke_mcp_action(ActuationIntent {
                    id: format!("{task_id}-release-gate"),
                    action: "safe.release.evaluate".to_string(),
                    target: "enterprise-release-candidate".to_string(),
                    requested_by: format!("a2a:{agent}"),
                    authority: "release-governance".to_string(),
                    parameters: BTreeMap::new(),
                });
                let completed = receipt.decision == "APPLIED";
                task.artifacts.push(artifact(
                    &task_id,
                    "release-evaluation",
                    "Release evaluation produced by an A2A agent through an MCP tool",
                    serde_json::to_value(&receipt).expect("receipt serialization must succeed"),
                ));
                task.state = if completed {
                    A2aTaskState::Completed
                } else {
                    A2aTaskState::Rejected
                };
                if !completed {
                    task.refusal = Some(receipt.code);
                }
            }
            "review-architecture" => {
                task.artifacts.push(artifact(
                    &task_id,
                    "architecture-review",
                    "Architecture runway observation; no direct actuation",
                    json!({
                        "architectureRisk": self.metrics.architecture_risk,
                        "enablerCapacityPct": self.metrics.enabler_capacity_pct,
                        "floorPct": self.config.architecture_enabler_floor_pct
                    }),
                ));
                task.state = A2aTaskState::Completed;
            }
            "authorize-budget" => {
                task.state = A2aTaskState::InputRequired;
                task.refusal = Some("HUMAN_AUTHORIZATION_REQUIRED".to_string());
            }
            _ => {
                task.state = A2aTaskState::Rejected;
                task.refusal = Some("A2A_SKILL_UNSUPPORTED".to_string());
            }
        }

        let mut terminal = BTreeMap::new();
        terminal.insert("agent".to_string(), agent.to_string());
        terminal.insert("skill".to_string(), skill.to_string());
        let task_state = task.state;
        terminal.insert("state".to_string(), format!("{task_state:?}"));
        if let Some(refusal) = &task.refusal {
            terminal.insert("refusal".to_string(), refusal.clone());
        }
        self.emit("protocol", "a2a.task-state", task_id.clone(), terminal);
        self.tasks.insert(task_id, task.clone());
        task
    }

    pub fn task(&self, id: &str) -> Option<&A2aTask> {
        self.tasks.get(id)
    }

    pub fn tasks(&self) -> Vec<&A2aTask> {
        self.tasks.values().collect()
    }

    pub fn cancel_task(&mut self, id: &str) -> Result<A2aTask, String> {
        let task = self
            .tasks
            .get_mut(id)
            .ok_or_else(|| "A2A_TASK_NOT_FOUND".to_string())?;
        match task.state {
            A2aTaskState::Submitted | A2aTaskState::Working | A2aTaskState::InputRequired => {
                task.state = A2aTaskState::Canceled;
                Ok(task.clone())
            }
            _ => Err("A2A_TERMINAL_TASK_IMMUTABLE".to_string()),
        }
    }

    pub fn run(mut self) -> SimulationReport {
        let mut initialized = BTreeMap::new();
        initialized.insert("mcp".to_string(), MCP_PROTOCOL_VERSION.to_string());
        initialized.insert("a2a".to_string(), A2A_PROTOCOL_VERSION.to_string());
        initialized.insert("teams".to_string(), self.scale.teams.to_string());
        initialized.insert(
            "team_people".to_string(),
            self.scale.team_people.to_string(),
        );
        initialized.insert(
            "topology_objects".to_string(),
            (self.scale.portfolios
                + self.scale.value_streams
                + self.scale.solution_trains
                + self.scale.arts
                + self.scale.teams)
                .to_string(),
        );
        self.emit(
            "admission",
            "enterprise.admitted",
            self.config.name.clone(),
            initialized,
        );

        let mut rng = DeterministicRng::new(self.scenario.seed);
        for pi in 1..=self.scenario.pi_count {
            self.metrics.release_ready = false;
            self.submit_a2a_task(
                "lean-portfolio-management-agent",
                "plan-pi",
                &format!("Plan PI {pi} for the admitted enterprise coordinate"),
            );
            let mut pi_detail = BTreeMap::new();
            pi_detail.insert("pi".to_string(), pi.to_string());
            self.emit("safe-cadence", "pi.started", format!("pi-{pi}"), pi_detail);

            for iteration in 1..=self.config.pi_iterations {
                self.apply_shocks(pi, iteration);
                self.observe_iteration(pi, iteration, &mut rng);

                let plans = autonomics::plan(&self.config, &self.metrics, pi, iteration);
                for plan in plans {
                    let mut detail = BTreeMap::new();
                    detail.insert("controller".to_string(), plan.controller);
                    detail.insert("observation".to_string(), plan.observation);
                    detail.insert("intent_id".to_string(), plan.intent.id.clone());
                    self.emit(
                        "autonomic",
                        "mape-k.plan",
                        plan.intent.target.clone(),
                        detail,
                    );
                    self.invoke_mcp_action(plan.intent);
                }

                let blocked_ratio = self
                    .metrics
                    .blocked_features
                    .saturating_mul(100)
                    .checked_div(self.metrics.active_features)
                    .unwrap_or(0);
                if blocked_ratio > 18 {
                    self.submit_a2a_task(
                        "solution-train-coordination-agent",
                        "resolve-dependency",
                        &format!(
                            "Resolve cross-ART dependency pressure at PI {pi} iteration {iteration}"
                        ),
                    );
                }
            }

            self.submit_a2a_task(
                "release-governance-agent",
                "evaluate-release",
                &format!("Evaluate the PI {pi} integrated release candidate"),
            );
            let mut pi_complete = BTreeMap::new();
            pi_complete.insert("pi".to_string(), pi.to_string());
            pi_complete.insert(
                "release_ready".to_string(),
                self.metrics.release_ready.to_string(),
            );
            self.emit(
                "safe-cadence",
                "pi.completed",
                format!("pi-{pi}"),
                pi_complete,
            );
        }

        let chain_valid = self.ledger.verify();
        let applied_receipts = self
            .ledger
            .entries()
            .iter()
            .filter(|entry| entry.event.kind == "actuation.applied")
            .count();
        let refused_receipts = self
            .ledger
            .entries()
            .iter()
            .filter(|entry| entry.event.kind == "actuation.refused")
            .count();
        let terminal_tasks = self.tasks.values().all(|task| {
            matches!(
                task.state,
                A2aTaskState::Completed
                    | A2aTaskState::Canceled
                    | A2aTaskState::Failed
                    | A2aTaskState::Rejected
                    | A2aTaskState::InputRequired
            )
        });
        let mut invariants = BTreeMap::new();
        invariants.insert("receipt_chain_valid".to_string(), chain_valid);
        invariants.insert(
            "zero_unreceipted_actuation".to_string(),
            applied_receipts == self.applied_actuations
                && refused_receipts == self.refused_actuations,
        );
        invariants.insert("a2a_tasks_terminal_or_waiting".to_string(), terminal_tasks);
        invariants.insert(
            "mcp_a2a_versions_bound".to_string(),
            MCP_PROTOCOL_VERSION == "2025-11-25" && A2A_PROTOCOL_VERSION == "1.0.0",
        );
        invariants.insert(
            "fortune5_scale_floor".to_string(),
            self.scale.teams >= 500 && self.scale.team_people >= 4_500,
        );
        invariants.insert(
            "topology_cardinality_exact".to_string(),
            self.topology.scale() == self.scale,
        );
        let standing = if invariants.values().all(|value| *value) {
            Standing::Alive
        } else {
            Standing::Blocked
        };
        let topology_digest = topology_digest(&self.topology);
        let replay_key = replay_key(
            &self.config,
            &self.scenario,
            &topology_digest,
            self.ledger.head(),
            &self.metrics,
        );
        SimulationReport {
            schema: "aps.safe-simulation-report.v26.7.30".to_string(),
            standing,
            enterprise: self.config.name,
            scenario: self.scenario.name,
            seed: self.scenario.seed,
            protocols: ProtocolProfile {
                mcp: MCP_PROTOCOL_VERSION.to_string(),
                a2a: A2A_PROTOCOL_VERSION.to_string(),
            },
            scale: self.scale,
            topology_digest,
            metrics: self.metrics,
            events: self.ledger.entries().len(),
            a2a_tasks: self.tasks.len(),
            applied_actuations: self.applied_actuations,
            refused_actuations: self.refused_actuations,
            receipt_head: self.ledger.head().to_string(),
            replay_key,
            invariants,
            nonclaims: vec![
                "This is a deterministic enterprise simulation, not a representation of any real Fortune 5 company".to_string(),
                "The MCP and A2A adapters implement bounded semantic profiles, not full transport or certification conformance".to_string(),
                "SAFe terminology is used for interoperability analysis; no affiliation or certification is claimed".to_string(),
                "Autonomic controllers cannot bypass the actuation broker or human authorization boundaries".to_string(),
            ],
        }
    }

    fn apply_shocks(&mut self, pi: u32, iteration: u32) {
        let shocks = self
            .scenario
            .shocks
            .iter()
            .filter(|shock| shock.pi == pi && shock.iteration == iteration)
            .cloned()
            .collect::<Vec<_>>();
        for shock in shocks {
            match shock.kind {
                ShockKind::RegulatoryDemand => {
                    self.metrics.compliance_risk =
                        self.metrics.compliance_risk.saturating_add(shock.magnitude);
                }
                ShockKind::DependencyWave | ShockKind::SupplierDelay => {
                    self.metrics.blocked_features = self
                        .metrics
                        .blocked_features
                        .saturating_add(shock.magnitude);
                }
                ShockKind::ProductionIncident => {
                    self.metrics.architecture_risk = self
                        .metrics
                        .architecture_risk
                        .saturating_add(shock.magnitude);
                    self.metrics.blocked_features = self
                        .metrics
                        .blocked_features
                        .saturating_add(shock.magnitude.saturating_div(2).max(1));
                }
                ShockKind::MarketSurge => {
                    self.metrics.active_features =
                        self.metrics.active_features.saturating_add(shock.magnitude);
                }
            }
            let mut detail = BTreeMap::new();
            detail.insert("pi".to_string(), pi.to_string());
            detail.insert("iteration".to_string(), iteration.to_string());
            let shock_kind = shock.kind;
            detail.insert("kind".to_string(), format!("{shock_kind:?}"));
            detail.insert("magnitude".to_string(), shock.magnitude.to_string());
            self.emit(
                "environment",
                "shock.observed",
                format!("pi-{pi}-iteration-{iteration}"),
                detail,
            );
        }
    }

    fn observe_iteration(&mut self, pi: u32, iteration: u32, rng: &mut DeterministicRng) {
        let available = self.metrics.active_features;
        let completion_target = 18 + rng.range(24);
        let completed = completion_target.min(available);
        self.metrics.active_features = self.metrics.active_features.saturating_sub(completed);
        self.metrics.completed_features = self.metrics.completed_features.saturating_add(completed);
        let intake = if self.metrics.intake_frozen {
            0
        } else {
            14 + rng.range(22)
        };
        self.metrics.active_features = self.metrics.active_features.saturating_add(intake);

        let unblock = 2 + rng.range(8);
        self.metrics.blocked_features = self.metrics.blocked_features.saturating_sub(unblock);
        if rng.range(100) < 26 {
            self.metrics.blocked_features = self
                .metrics
                .blocked_features
                .saturating_add(1 + rng.range(5));
        }
        if rng.range(100) < 22 {
            self.metrics.architecture_risk = self.metrics.architecture_risk.saturating_add(1);
        } else if self.metrics.enabler_capacity_pct >= self.config.architecture_enabler_floor_pct {
            self.metrics.architecture_risk = self.metrics.architecture_risk.saturating_sub(1);
        }
        if rng.range(100) < 12 {
            self.metrics.compliance_risk = self.metrics.compliance_risk.saturating_add(1);
        } else {
            self.metrics.compliance_risk = self.metrics.compliance_risk.saturating_sub(1);
        }
        self.metrics.budget_consumed_pct = self
            .metrics
            .budget_consumed_pct
            .saturating_add((1 + rng.range(3)) as u8)
            .min(100);

        let mut detail = BTreeMap::new();
        detail.insert("pi".to_string(), pi.to_string());
        detail.insert("iteration".to_string(), iteration.to_string());
        detail.insert("completed".to_string(), completed.to_string());
        detail.insert("intake".to_string(), intake.to_string());
        detail.insert(
            "active_features".to_string(),
            self.metrics.active_features.to_string(),
        );
        detail.insert(
            "blocked_features".to_string(),
            self.metrics.blocked_features.to_string(),
        );
        detail.insert(
            "budget_consumed_pct".to_string(),
            self.metrics.budget_consumed_pct.to_string(),
        );
        self.emit(
            "safe-cadence",
            "iteration.observed",
            format!("pi-{pi}-iteration-{iteration}"),
            detail,
        );
    }
}

fn artifact(task_id: &str, name: &str, description: &str, data: serde_json::Value) -> A2aArtifact {
    A2aArtifact {
        artifact_id: format!("{task_id}:{name}"),
        name: name.to_string(),
        description: description.to_string(),
        parts: vec![A2aPart {
            kind: "data".to_string(),
            text: None,
            data: Some(data),
        }],
    }
}

fn topology_digest(topology: &EnterpriseTopology) -> String {
    let bytes = serde_json::to_vec(topology).expect("topology serialization must succeed");
    let digest = Sha256::digest(bytes);
    digest.iter().map(|byte| format!("{byte:02x}")).collect()
}

fn replay_key(
    config: &EnterpriseConfig,
    scenario: &ScenarioConfig,
    topology_digest: &str,
    head: &str,
    metrics: &Metrics,
) -> String {
    let material = json!({
        "config": config,
        "scenario": scenario,
        "topologyDigest": topology_digest,
        "head": head,
        "metrics": metrics,
    });
    let bytes = serde_json::to_vec(&material).expect("replay material serialization must succeed");
    let digest = Sha256::digest(bytes);
    digest.iter().map(|byte| format!("{byte:02x}")).collect()
}

#[derive(Debug, Clone)]
struct DeterministicRng {
    state: u64,
}

impl DeterministicRng {
    fn new(seed: u64) -> Self {
        Self {
            state: seed ^ 0x9E37_79B9_7F4A_7C15,
        }
    }

    fn next(&mut self) -> u32 {
        self.state = self
            .state
            .wrapping_mul(6_364_136_223_846_793_005)
            .wrapping_add(1_442_695_040_888_963_407);
        (self.state >> 32) as u32
    }

    fn range(&mut self, upper: u32) -> u32 {
        if upper == 0 { 0 } else { self.next() % upper }
    }
}

pub fn compare_reports(
    left: &SimulationReport,
    right: &SimulationReport,
) -> BTreeMap<&'static str, bool> {
    BTreeMap::from([
        ("standing", left.standing == right.standing),
        ("metrics", left.metrics == right.metrics),
        ("events", left.events == right.events),
        (
            "topology_digest",
            left.topology_digest == right.topology_digest,
        ),
        ("receipt_head", left.receipt_head == right.receipt_head),
        ("replay_key", left.replay_key == right.replay_key),
    ])
}

use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;

pub const MCP_PROTOCOL_VERSION: &str = "2025-11-25";
pub const A2A_PROTOCOL_VERSION: &str = "1.0.0";

#[derive(Debug, Clone, Copy, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "SCREAMING_SNAKE_CASE")]
pub enum Standing {
    PartialAlive,
    Alive,
    Blocked,
    BuildBroken,
    Unknown,
    Unsupported,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct EnterpriseConfig {
    pub schema: String,
    pub name: String,
    pub portfolios: u32,
    pub value_streams_per_portfolio: u32,
    pub solution_trains_per_value_stream: u32,
    pub arts_per_solution_train: u32,
    pub teams_per_art: u32,
    pub people_per_team: u32,
    pub pi_iterations: u32,
    pub iteration_days: u32,
    pub portfolio_wip_limit: u32,
    pub architecture_enabler_floor_pct: u8,
    pub compliance_risk_tolerance: u32,
    pub autonomics: AutonomicPolicy,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct AutonomicPolicy {
    pub wip_unfreeze_threshold_pct: u8,
    pub dependency_blocked_ratio_bps: u32,
    pub capacity_rebalance_delta_pct: u8,
    pub max_capacity_rebalance_delta_pct: u8,
    pub architecture_risk_threshold: u32,
    pub architecture_enabler_ceiling_pct: u8,
    pub budget_escalation_pct: u8,
    pub budget_request_delta_pct: u8,
    pub max_budget_reallocation_delta_pct: u8,
    pub release_blocked_ratio_pct: u8,
}

impl AutonomicPolicy {
    fn validate(&self) -> Result<(), String> {
        if self.wip_unfreeze_threshold_pct == 0 || self.wip_unfreeze_threshold_pct > 100 {
            return Err("WIP unfreeze threshold must be between 1 and 100".to_string());
        }
        if self.dependency_blocked_ratio_bps == 0 || self.dependency_blocked_ratio_bps > 10_000 {
            return Err("dependency ratio must be between 1 and 10000 basis points".to_string());
        }
        if self.capacity_rebalance_delta_pct == 0
            || self.capacity_rebalance_delta_pct > self.max_capacity_rebalance_delta_pct
            || self.max_capacity_rebalance_delta_pct > 25
        {
            return Err("capacity rebalance policy is outside its bounded ceiling".to_string());
        }
        if self.architecture_enabler_ceiling_pct == 0 || self.architecture_enabler_ceiling_pct > 50
        {
            return Err("architecture enabler ceiling must be between 1 and 50".to_string());
        }
        if self.budget_escalation_pct == 0 || self.budget_escalation_pct > 100 {
            return Err("budget escalation threshold must be between 1 and 100".to_string());
        }
        if self.budget_request_delta_pct == 0
            || self.budget_request_delta_pct > self.max_budget_reallocation_delta_pct
            || self.max_budget_reallocation_delta_pct > 25
        {
            return Err("budget reallocation policy is outside its bounded ceiling".to_string());
        }
        if self.release_blocked_ratio_pct == 0 || self.release_blocked_ratio_pct > 100 {
            return Err("release blocked ratio must be between 1 and 100".to_string());
        }
        Ok(())
    }
}

impl EnterpriseConfig {
    pub fn validate(&self) -> Result<(), String> {
        if self.schema != "aps.safe-enterprise.v26.7.30" {
            return Err("enterprise schema must be aps.safe-enterprise.v26.7.30".to_string());
        }
        if self.name.trim().is_empty() {
            return Err("enterprise name must not be empty".to_string());
        }
        let positive = [
            self.portfolios,
            self.value_streams_per_portfolio,
            self.solution_trains_per_value_stream,
            self.arts_per_solution_train,
            self.teams_per_art,
            self.people_per_team,
            self.pi_iterations,
            self.iteration_days,
            self.portfolio_wip_limit,
        ];
        if positive.contains(&0) {
            return Err("enterprise cardinalities must be positive".to_string());
        }
        if self.architecture_enabler_floor_pct > 50
            || self.architecture_enabler_floor_pct
                > self.autonomics.architecture_enabler_ceiling_pct
        {
            return Err(
                "architecture enabler floor must be within the autonomic ceiling".to_string(),
            );
        }
        self.autonomics.validate()?;
        let scale = self.scale();
        if scale.teams < 500 {
            return Err(
                "Fortune-5-scale profile requires at least 500 simulated teams".to_string(),
            );
        }
        Ok(())
    }

    pub fn scale(&self) -> EnterpriseScale {
        let value_streams = self.portfolios * self.value_streams_per_portfolio;
        let solution_trains = value_streams * self.solution_trains_per_value_stream;
        let arts = solution_trains * self.arts_per_solution_train;
        let teams = arts * self.teams_per_art;
        let team_people = teams * self.people_per_team;
        EnterpriseScale {
            portfolios: self.portfolios,
            value_streams,
            solution_trains,
            arts,
            teams,
            team_people,
        }
    }

    pub fn topology(&self) -> EnterpriseTopology {
        let mut portfolios = Vec::with_capacity(self.portfolios as usize);
        for portfolio_index in 1..=self.portfolios {
            let portfolio_id = format!("portfolio-{portfolio_index:02}");
            let mut value_streams = Vec::with_capacity(self.value_streams_per_portfolio as usize);
            for value_stream_index in 1..=self.value_streams_per_portfolio {
                let value_stream_id =
                    format!("{portfolio_id}-value-stream-{value_stream_index:02}");
                let mut solution_trains =
                    Vec::with_capacity(self.solution_trains_per_value_stream as usize);
                for solution_train_index in 1..=self.solution_trains_per_value_stream {
                    let solution_train_id =
                        format!("{value_stream_id}-solution-train-{solution_train_index:02}");
                    let mut arts = Vec::with_capacity(self.arts_per_solution_train as usize);
                    for art_index in 1..=self.arts_per_solution_train {
                        let art_id = format!("{solution_train_id}-art-{art_index:02}");
                        let mut teams = Vec::with_capacity(self.teams_per_art as usize);
                        for team_index in 1..=self.teams_per_art {
                            teams.push(TeamNode {
                                id: format!("{art_id}-team-{team_index:02}"),
                                name: format!(
                                    "Team P{portfolio_index:02}-V{value_stream_index:02}-S{solution_train_index:02}-A{art_index:02}-T{team_index:02}"
                                ),
                                people: self.people_per_team,
                            });
                        }
                        arts.push(AgileReleaseTrainNode {
                            id: art_id,
                            name: format!(
                                "ART P{portfolio_index:02}-V{value_stream_index:02}-S{solution_train_index:02}-A{art_index:02}"
                            ),
                            teams,
                        });
                    }
                    solution_trains.push(SolutionTrainNode {
                        id: solution_train_id,
                        name: format!(
                            "Solution Train P{portfolio_index:02}-V{value_stream_index:02}-S{solution_train_index:02}"
                        ),
                        arts,
                    });
                }
                value_streams.push(ValueStreamNode {
                    id: value_stream_id,
                    name: format!(
                        "Development Value Stream P{portfolio_index:02}-V{value_stream_index:02}"
                    ),
                    solution_trains,
                });
            }
            portfolios.push(PortfolioNode {
                id: portfolio_id,
                name: format!("Portfolio {portfolio_index:02}"),
                value_streams,
            });
        }
        EnterpriseTopology {
            enterprise: self.name.clone(),
            portfolios,
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct EnterpriseScale {
    pub portfolios: u32,
    pub value_streams: u32,
    pub solution_trains: u32,
    pub arts: u32,
    pub teams: u32,
    pub team_people: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct EnterpriseTopology {
    pub enterprise: String,
    pub portfolios: Vec<PortfolioNode>,
}

impl EnterpriseTopology {
    pub fn scale(&self) -> EnterpriseScale {
        let portfolios = self.portfolios.len() as u32;
        let value_streams = self
            .portfolios
            .iter()
            .map(|portfolio| portfolio.value_streams.len() as u32)
            .sum();
        let solution_trains = self
            .portfolios
            .iter()
            .flat_map(|portfolio| &portfolio.value_streams)
            .map(|value_stream| value_stream.solution_trains.len() as u32)
            .sum();
        let arts = self
            .portfolios
            .iter()
            .flat_map(|portfolio| &portfolio.value_streams)
            .flat_map(|value_stream| &value_stream.solution_trains)
            .map(|solution_train| solution_train.arts.len() as u32)
            .sum();
        let teams = self
            .portfolios
            .iter()
            .flat_map(|portfolio| &portfolio.value_streams)
            .flat_map(|value_stream| &value_stream.solution_trains)
            .flat_map(|solution_train| &solution_train.arts)
            .map(|art| art.teams.len() as u32)
            .sum();
        let team_people = self
            .portfolios
            .iter()
            .flat_map(|portfolio| &portfolio.value_streams)
            .flat_map(|value_stream| &value_stream.solution_trains)
            .flat_map(|solution_train| &solution_train.arts)
            .flat_map(|art| &art.teams)
            .map(|team| team.people)
            .sum();
        EnterpriseScale {
            portfolios,
            value_streams,
            solution_trains,
            arts,
            teams,
            team_people,
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct PortfolioNode {
    pub id: String,
    pub name: String,
    pub value_streams: Vec<ValueStreamNode>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct ValueStreamNode {
    pub id: String,
    pub name: String,
    pub solution_trains: Vec<SolutionTrainNode>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct SolutionTrainNode {
    pub id: String,
    pub name: String,
    pub arts: Vec<AgileReleaseTrainNode>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct AgileReleaseTrainNode {
    pub id: String,
    pub name: String,
    pub teams: Vec<TeamNode>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct TeamNode {
    pub id: String,
    pub name: String,
    pub people: u32,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ScenarioConfig {
    pub schema: String,
    pub name: String,
    pub seed: u64,
    pub pi_count: u32,
    pub initial: InitialMetrics,
    pub shocks: Vec<Shock>,
}

impl ScenarioConfig {
    pub fn validate(&self) -> Result<(), String> {
        if self.schema != "aps.safe-scenario.v26.7.30" {
            return Err("scenario schema must be aps.safe-scenario.v26.7.30".to_string());
        }
        if self.name.trim().is_empty() || self.pi_count == 0 {
            return Err("scenario name and PI count are required".to_string());
        }
        if self.initial.budget_consumed_pct > 100 || self.initial.enabler_capacity_pct > 100 {
            return Err("percentage metrics must be between 0 and 100".to_string());
        }
        if self
            .shocks
            .iter()
            .any(|shock| shock.pi == 0 || shock.iteration == 0 || shock.magnitude == 0)
        {
            return Err("shock coordinates and magnitude must be positive".to_string());
        }
        Ok(())
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct InitialMetrics {
    pub active_features: u32,
    pub blocked_features: u32,
    pub architecture_risk: u32,
    pub compliance_risk: u32,
    pub budget_consumed_pct: u8,
    pub enabler_capacity_pct: u8,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct Shock {
    pub pi: u32,
    pub iteration: u32,
    pub kind: ShockKind,
    pub magnitude: u32,
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "kebab-case")]
pub enum ShockKind {
    RegulatoryDemand,
    DependencyWave,
    ProductionIncident,
    MarketSurge,
    SupplierDelay,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct Metrics {
    pub active_features: u32,
    pub blocked_features: u32,
    pub completed_features: u32,
    pub architecture_risk: u32,
    pub compliance_risk: u32,
    pub budget_consumed_pct: u8,
    pub enabler_capacity_pct: u8,
    pub capacity_rebalanced_pct: u8,
    pub intake_frozen: bool,
    pub release_ready: bool,
}

impl From<&InitialMetrics> for Metrics {
    fn from(initial: &InitialMetrics) -> Self {
        Self {
            active_features: initial.active_features,
            blocked_features: initial.blocked_features,
            completed_features: 0,
            architecture_risk: initial.architecture_risk,
            compliance_risk: initial.compliance_risk,
            budget_consumed_pct: initial.budget_consumed_pct,
            enabler_capacity_pct: initial.enabler_capacity_pct,
            capacity_rebalanced_pct: 0,
            intake_frozen: false,
            release_ready: false,
        }
    }
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct Event {
    pub sequence: u64,
    pub phase: String,
    pub kind: String,
    pub subject: String,
    pub detail: BTreeMap<String, String>,
}

impl Event {
    pub fn new(
        phase: impl Into<String>,
        kind: impl Into<String>,
        subject: impl Into<String>,
        detail: BTreeMap<String, String>,
    ) -> Self {
        Self {
            sequence: 0,
            phase: phase.into(),
            kind: kind.into(),
            subject: subject.into(),
            detail,
        }
    }
}

#[derive(Debug, Clone, Copy, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "kebab-case")]
pub enum A2aTaskState {
    Submitted,
    Working,
    InputRequired,
    Completed,
    Canceled,
    Failed,
    Rejected,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct A2aPart {
    pub kind: String,
    pub text: Option<String>,
    pub data: Option<serde_json::Value>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct A2aMessage {
    pub role: String,
    pub parts: Vec<A2aPart>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct A2aArtifact {
    pub artifact_id: String,
    pub name: String,
    pub description: String,
    pub parts: Vec<A2aPart>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct A2aTask {
    pub id: String,
    pub context_id: String,
    pub agent: String,
    pub skill: String,
    pub state: A2aTaskState,
    pub history: Vec<A2aMessage>,
    pub artifacts: Vec<A2aArtifact>,
    pub refusal: Option<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ProtocolProfile {
    pub mcp: String,
    pub a2a: String,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct SimulationReport {
    pub schema: String,
    pub standing: Standing,
    pub enterprise: String,
    pub scenario: String,
    pub seed: u64,
    pub protocols: ProtocolProfile,
    pub scale: EnterpriseScale,
    pub topology_digest: String,
    pub metrics: Metrics,
    pub events: usize,
    pub a2a_tasks: usize,
    pub applied_actuations: usize,
    pub refused_actuations: usize,
    pub receipt_head: String,
    pub replay_key: String,
    pub invariants: BTreeMap<String, bool>,
    pub nonclaims: Vec<String>,
}

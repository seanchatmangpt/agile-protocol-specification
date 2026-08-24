use crate::ledger::ReceiptLedger;
use crate::model::{EnterpriseConfig, Event, Metrics, Standing};
use serde::{Deserialize, Serialize};
use std::collections::BTreeMap;

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ActuationIntent {
    pub id: String,
    pub action: String,
    pub target: String,
    pub requested_by: String,
    pub authority: String,
    #[serde(default)]
    pub parameters: BTreeMap<String, String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct ActuationReceipt {
    pub schema: String,
    pub intent_id: String,
    pub action: String,
    pub decision: String,
    pub standing: Standing,
    pub code: String,
    pub before: Metrics,
    pub after: Metrics,
    pub event_hash: String,
}

pub fn submit(
    config: &EnterpriseConfig,
    metrics: &mut Metrics,
    ledger: &mut ReceiptLedger,
    intent: ActuationIntent,
) -> ActuationReceipt {
    let before = metrics.clone();
    let mut decision = "REFUSED".to_string();
    let mut standing = Standing::Blocked;
    let code = match intent.action.as_str() {
        "safe.portfolio.freeze-intake" => {
            if !allowed(
                &intent.authority,
                &["lean-portfolio-management", "autonomic-wip-guard"],
            ) {
                "AUTHORITY_REFUSED".to_string()
            } else if metrics.active_features <= config.portfolio_wip_limit {
                "PRECONDITION_FALSE".to_string()
            } else {
                metrics.intake_frozen = true;
                decision = "APPLIED".to_string();
                standing = Standing::Alive;
                "INTAKE_FROZEN".to_string()
            }
        }
        "safe.portfolio.unfreeze-intake" => {
            if !allowed(
                &intent.authority,
                &["lean-portfolio-management", "autonomic-wip-guard"],
            ) {
                "AUTHORITY_REFUSED".to_string()
            } else if metrics.active_features > config.portfolio_wip_limit.saturating_mul(9) / 10 {
                "WIP_STILL_ELEVATED".to_string()
            } else {
                metrics.intake_frozen = false;
                decision = "APPLIED".to_string();
                standing = Standing::Alive;
                "INTAKE_UNFROZEN".to_string()
            }
        }
        "safe.capacity.rebalance" => {
            if !allowed(
                &intent.authority,
                &["release-train-engineer", "autonomic-dependency-controller"],
            ) {
                "AUTHORITY_REFUSED".to_string()
            } else {
                let delta = parameter_u8(&intent, "delta_pct").unwrap_or(0);
                if delta == 0 || delta > config.autonomics.max_capacity_rebalance_delta_pct {
                    "BOUNDED_DELTA_REFUSED".to_string()
                } else {
                    metrics.capacity_rebalanced_pct = metrics
                        .capacity_rebalanced_pct
                        .saturating_add(delta)
                        .min(25);
                    let reduction = u32::from(delta).saturating_mul(2);
                    metrics.blocked_features = metrics.blocked_features.saturating_sub(reduction);
                    decision = "APPLIED".to_string();
                    standing = Standing::Alive;
                    "CAPACITY_REBALANCED".to_string()
                }
            }
        }
        "safe.architecture.allocate-enabler" => {
            if !allowed(
                &intent.authority,
                &["enterprise-architect", "autonomic-runway-controller"],
            ) {
                "AUTHORITY_REFUSED".to_string()
            } else {
                let target = parameter_u8(&intent, "target_pct").unwrap_or(0);
                if target < config.architecture_enabler_floor_pct
                    || target > config.autonomics.architecture_enabler_ceiling_pct
                {
                    "ENABLER_GUARDRAIL_REFUSED".to_string()
                } else {
                    metrics.enabler_capacity_pct = target;
                    metrics.architecture_risk = metrics.architecture_risk.saturating_sub(2);
                    decision = "APPLIED".to_string();
                    standing = Standing::Alive;
                    "ENABLER_CAPACITY_ALLOCATED".to_string()
                }
            }
        }
        "safe.release.evaluate" => {
            if !allowed(
                &intent.authority,
                &["release-governance", "autonomic-compliance-gate"],
            ) {
                "AUTHORITY_REFUSED".to_string()
            } else if metrics.compliance_risk > config.compliance_risk_tolerance {
                metrics.release_ready = false;
                "COMPLIANCE_GATE_REFUSED".to_string()
            } else if metrics.blocked_features.saturating_mul(100)
                > metrics
                    .active_features
                    .saturating_mul(u32::from(config.autonomics.release_blocked_ratio_pct))
            {
                metrics.release_ready = false;
                "FLOW_GATE_REFUSED".to_string()
            } else {
                metrics.release_ready = true;
                decision = "APPLIED".to_string();
                standing = Standing::Alive;
                "RELEASE_CANDIDATE_ADMITTED".to_string()
            }
        }
        "safe.budget.reallocate" => {
            if intent.authority != "human-investment-committee" {
                "HUMAN_AUTHORIZATION_REQUIRED".to_string()
            } else {
                let delta = parameter_u8(&intent, "delta_pct").unwrap_or(0);
                if delta == 0 || delta > config.autonomics.max_budget_reallocation_delta_pct {
                    "BUDGET_GUARDRAIL_REFUSED".to_string()
                } else {
                    metrics.budget_consumed_pct = metrics.budget_consumed_pct.saturating_sub(delta);
                    decision = "APPLIED".to_string();
                    standing = Standing::Alive;
                    "BUDGET_REALLOCATED".to_string()
                }
            }
        }
        _ => {
            standing = Standing::Unsupported;
            "ACTION_UNSUPPORTED".to_string()
        }
    };

    let after = metrics.clone();
    let mut detail = BTreeMap::new();
    detail.insert("intent_id".to_string(), intent.id.clone());
    detail.insert("action".to_string(), intent.action.clone());
    detail.insert("target".to_string(), intent.target.clone());
    detail.insert("requested_by".to_string(), intent.requested_by.clone());
    detail.insert("authority".to_string(), intent.authority.clone());
    detail.insert("decision".to_string(), decision.clone());
    detail.insert("code".to_string(), code.clone());
    let event_hash = ledger.append(Event::new(
        "actuation",
        if decision == "APPLIED" {
            "actuation.applied"
        } else {
            "actuation.refused"
        },
        intent.target,
        detail,
    ));

    ActuationReceipt {
        schema: "aps.actuation-receipt.v26.7.30".to_string(),
        intent_id: intent.id,
        action: intent.action,
        decision,
        standing,
        code,
        before,
        after,
        event_hash,
    }
}

fn allowed(authority: &str, allowed: &[&str]) -> bool {
    allowed.contains(&authority)
}

fn parameter_u8(intent: &ActuationIntent, name: &str) -> Option<u8> {
    intent.parameters.get(name)?.parse().ok()
}

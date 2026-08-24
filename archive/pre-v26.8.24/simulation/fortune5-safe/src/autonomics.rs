use crate::broker::ActuationIntent;
use crate::model::{EnterpriseConfig, Metrics};
use std::collections::BTreeMap;

#[derive(Debug, Clone, PartialEq, Eq)]
pub struct AutonomicPlan {
    pub controller: String,
    pub observation: String,
    pub intent: ActuationIntent,
}

pub fn plan(
    config: &EnterpriseConfig,
    metrics: &Metrics,
    pi: u32,
    iteration: u32,
) -> Vec<AutonomicPlan> {
    let mut plans = Vec::new();

    if metrics.active_features > config.portfolio_wip_limit && !metrics.intake_frozen {
        plans.push(AutonomicPlan {
            controller: "wip-guard".to_string(),
            observation: format!(
                "active_features={} exceeds portfolio_wip_limit={}",
                metrics.active_features, config.portfolio_wip_limit
            ),
            intent: intent(
                pi,
                iteration,
                "wip-guard",
                "safe.portfolio.freeze-intake",
                "portfolio-kanban",
                "autonomic-wip-guard",
                BTreeMap::new(),
            ),
        });
    }

    if metrics.intake_frozen
        && metrics.active_features.saturating_mul(100)
            <= config
                .portfolio_wip_limit
                .saturating_mul(u32::from(config.autonomics.wip_unfreeze_threshold_pct))
    {
        plans.push(AutonomicPlan {
            controller: "wip-guard".to_string(),
            observation: "portfolio WIP returned below the bounded release threshold".to_string(),
            intent: intent(
                pi,
                iteration,
                "wip-unfreeze",
                "safe.portfolio.unfreeze-intake",
                "portfolio-kanban",
                "autonomic-wip-guard",
                BTreeMap::new(),
            ),
        });
    }

    let blocked_ratio_basis_points = metrics
        .blocked_features
        .saturating_mul(10_000)
        .checked_div(metrics.active_features)
        .unwrap_or(0);
    if blocked_ratio_basis_points > config.autonomics.dependency_blocked_ratio_bps {
        let mut parameters = BTreeMap::new();
        parameters.insert(
            "delta_pct".to_string(),
            config.autonomics.capacity_rebalance_delta_pct.to_string(),
        );
        plans.push(AutonomicPlan {
            controller: "dependency-controller".to_string(),
            observation: format!(
                "blocked ratio is {} basis points",
                blocked_ratio_basis_points
            ),
            intent: intent(
                pi,
                iteration,
                "dependency-rebalance",
                "safe.capacity.rebalance",
                "solution-train-capacity",
                "autonomic-dependency-controller",
                parameters,
            ),
        });
    }

    if metrics.architecture_risk > config.autonomics.architecture_risk_threshold
        && metrics.enabler_capacity_pct < config.architecture_enabler_floor_pct
    {
        let mut parameters = BTreeMap::new();
        parameters.insert(
            "target_pct".to_string(),
            config.architecture_enabler_floor_pct.to_string(),
        );
        plans.push(AutonomicPlan {
            controller: "runway-controller".to_string(),
            observation: format!(
                "architecture risk {} exceeds threshold while enabler capacity is {} percent",
                metrics.architecture_risk, metrics.enabler_capacity_pct
            ),
            intent: intent(
                pi,
                iteration,
                "architecture-runway",
                "safe.architecture.allocate-enabler",
                "architecture-runway",
                "autonomic-runway-controller",
                parameters,
            ),
        });
    }

    if metrics.budget_consumed_pct >= config.autonomics.budget_escalation_pct {
        let mut parameters = BTreeMap::new();
        parameters.insert(
            "delta_pct".to_string(),
            config.autonomics.budget_request_delta_pct.to_string(),
        );
        plans.push(AutonomicPlan {
            controller: "budget-watch".to_string(),
            observation: format!(
                "budget consumption reached {} percent",
                metrics.budget_consumed_pct
            ),
            intent: intent(
                pi,
                iteration,
                "budget-reallocation-request",
                "safe.budget.reallocate",
                "lean-budget",
                "autonomic-budget-controller",
                parameters,
            ),
        });
    }

    plans
}

fn intent(
    pi: u32,
    iteration: u32,
    suffix: &str,
    action: &str,
    target: &str,
    authority: &str,
    parameters: BTreeMap<String, String>,
) -> ActuationIntent {
    ActuationIntent {
        id: format!("intent-pi{pi}-it{iteration}-{suffix}"),
        action: action.to_string(),
        target: target.to_string(),
        requested_by: format!("autonomic:{suffix}"),
        authority: authority.to_string(),
        parameters,
    }
}

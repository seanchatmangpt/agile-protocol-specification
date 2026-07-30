pub mod a2a;
pub mod autonomics;
pub mod broker;
pub mod engine;
pub mod ledger;
pub mod mcp;
pub mod model;

use crate::model::{EnterpriseConfig, ScenarioConfig};
use std::fs;
use std::path::Path;

pub fn load_enterprise_config(path: impl AsRef<Path>) -> Result<EnterpriseConfig, String> {
    let text = fs::read_to_string(path.as_ref())
        .map_err(|error| format!("failed to read enterprise config: {error}"))?;
    let config: EnterpriseConfig = serde_json::from_str(&text)
        .map_err(|error| format!("failed to parse enterprise config: {error}"))?;
    config.validate()?;
    Ok(config)
}

pub fn load_scenario_config(path: impl AsRef<Path>) -> Result<ScenarioConfig, String> {
    let text = fs::read_to_string(path.as_ref())
        .map_err(|error| format!("failed to read scenario config: {error}"))?;
    let scenario: ScenarioConfig = serde_json::from_str(&text)
        .map_err(|error| format!("failed to parse scenario config: {error}"))?;
    scenario.validate()?;
    Ok(scenario)
}

use aps_fortune5_safe_sim::a2a;
use aps_fortune5_safe_sim::broker::ActuationIntent;
use aps_fortune5_safe_sim::engine::{EnterpriseEngine, compare_reports};
use aps_fortune5_safe_sim::mcp;
use aps_fortune5_safe_sim::model::Standing;
use aps_fortune5_safe_sim::{load_enterprise_config, load_scenario_config};
use serde_json::{Value, json};
use std::collections::BTreeMap;
use std::path::PathBuf;

fn fixtures() -> (PathBuf, PathBuf) {
    let root = PathBuf::from(env!("CARGO_MANIFEST_DIR"));
    (
        root.join("config/fortune5-enterprise.json"),
        root.join("config/global-core-modernization.json"),
    )
}

fn engine() -> EnterpriseEngine {
    let (config, scenario) = fixtures();
    EnterpriseEngine::new(
        load_enterprise_config(config).expect("valid enterprise config"),
        load_scenario_config(scenario).expect("valid scenario config"),
    )
    .expect("valid engine")
}

#[test]
fn topology_materializes_exact_enterprise_object_graph() {
    let engine = engine();
    let scale = engine.topology.scale();
    assert_eq!(scale, engine.scale);
    assert_eq!(scale.portfolios, 5);
    assert_eq!(scale.value_streams, 20);
    assert_eq!(scale.solution_trains, 40);
    assert_eq!(scale.arts, 80);
    assert_eq!(scale.teams, 800);
    assert_eq!(scale.team_people, 7_200);
}

#[test]
fn deterministic_replay_has_identical_receipt_head() {
    let (config, scenario) = fixtures();
    let config = load_enterprise_config(config).expect("valid enterprise config");
    let scenario = load_scenario_config(scenario).expect("valid scenario config");
    let first = EnterpriseEngine::new(config.clone(), scenario.clone())
        .expect("valid engine")
        .run();
    let second = EnterpriseEngine::new(config, scenario)
        .expect("valid engine")
        .run();
    assert!(
        compare_reports(&first, &second)
            .values()
            .all(|value| *value)
    );
    assert_eq!(first.standing, Standing::Alive);
}

#[test]
fn mcp_initialization_negotiates_exact_version() {
    let mut engine = engine();
    let response = mcp::handle(
        &mut engine,
        &json!({
            "jsonrpc":"2.0",
            "id":1,
            "method":"initialize",
            "params":{
                "protocolVersion":"2025-11-25",
                "capabilities":{},
                "clientInfo":{"name":"test","version":"1"}
            }
        }),
    );
    assert_eq!(
        response
            .pointer("/result/protocolVersion")
            .and_then(Value::as_str),
        Some("2025-11-25")
    );
}

#[test]
fn mcp_autonomous_budget_change_is_refused() {
    let mut engine = engine();
    let response = mcp::handle(
        &mut engine,
        &json!({
            "jsonrpc":"2.0",
            "id":2,
            "method":"tools/call",
            "params":{
                "name":"safe.budget.reallocate",
                "arguments":{
                    "authority":"autonomic-budget-controller",
                    "delta_pct":5,
                    "target":"lean-budget"
                }
            }
        }),
    );
    assert_eq!(
        response
            .pointer("/result/structuredContent/code")
            .and_then(Value::as_str),
        Some("HUMAN_AUTHORIZATION_REQUIRED")
    );
    assert_eq!(
        response.pointer("/result/isError").and_then(Value::as_bool),
        Some(true)
    );
}

#[test]
fn broker_rejects_unbounded_capacity_delta() {
    let mut engine = engine();
    let mut parameters = BTreeMap::new();
    parameters.insert("delta_pct".to_string(), "9".to_string());
    let receipt = engine.invoke_mcp_action(ActuationIntent {
        id: "negative-unbounded-capacity".to_string(),
        action: "safe.capacity.rebalance".to_string(),
        target: "solution-train-capacity".to_string(),
        requested_by: "test".to_string(),
        authority: "release-train-engineer".to_string(),
        parameters,
    });
    assert_eq!(receipt.decision, "REFUSED");
    assert_eq!(receipt.code, "BOUNDED_DELTA_REFUSED");
}

#[test]
fn a2a_task_returns_artifact_not_message_output() {
    let mut engine = engine();
    let response = a2a::handle(
        &mut engine,
        &json!({
            "jsonrpc":"2.0",
            "id":3,
            "method":"message/send",
            "params":{
                "agent":"lean-portfolio-management-agent",
                "skill":"plan-pi",
                "message":{
                    "role":"user",
                    "parts":[{"kind":"text","text":"Plan the next PI"}]
                }
            }
        }),
    );
    assert_eq!(
        response.pointer("/result/state").and_then(Value::as_str),
        Some("completed")
    );
    assert!(
        response
            .pointer("/result/artifacts/0/parts/0/data")
            .is_some()
    );
}

#[test]
fn terminal_a2a_task_cannot_be_canceled() {
    let mut engine = engine();
    let task = engine.submit_a2a_task(
        "lean-portfolio-management-agent",
        "plan-pi",
        "Plan the next PI",
    );
    let response = a2a::handle(
        &mut engine,
        &json!({
            "jsonrpc":"2.0",
            "id":4,
            "method":"tasks/cancel",
            "params":{"id":task.id}
        }),
    );
    assert_eq!(
        response.pointer("/error/message").and_then(Value::as_str),
        Some("A2A_TERMINAL_TASK_IMMUTABLE")
    );
}

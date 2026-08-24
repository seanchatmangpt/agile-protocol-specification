use aps_fortune5_safe_sim::a2a;
use aps_fortune5_safe_sim::broker::ActuationIntent;
use aps_fortune5_safe_sim::engine::{EnterpriseEngine, compare_reports};
use aps_fortune5_safe_sim::mcp;
use aps_fortune5_safe_sim::model::Standing;
use aps_fortune5_safe_sim::{load_enterprise_config, load_scenario_config};
use serde_json::{Value, json};
use std::collections::BTreeMap;
use std::env;
use std::error::Error;
use std::fs;
use std::io::{self, BufRead, Write};
use std::path::{Path, PathBuf};

fn main() -> Result<(), Box<dyn Error>> {
    let args = env::args().skip(1).collect::<Vec<_>>();
    let command = args.first().map(String::as_str).unwrap_or("help");
    match command {
        "simulate" => simulate(&args[1..])?,
        "mcp-fixture" => protocol_fixture(&args[1..], Protocol::Mcp)?,
        "a2a-fixture" => protocol_fixture(&args[1..], Protocol::A2a)?,
        "mcp-stdio" => protocol_stdio(&args[1..], Protocol::Mcp)?,
        "a2a-jsonl" => protocol_stdio(&args[1..], Protocol::A2a)?,
        "agent-cards" => print_json(&serde_json::to_value(a2a::agent_cards())?)?,
        "self-test" => self_test(&args[1..])?,
        _ => print_help(),
    }
    Ok(())
}

fn simulate(args: &[String]) -> Result<(), Box<dyn Error>> {
    let (config_path, scenario_path) = config_paths(args);
    let output = option(args, "--out").map(PathBuf::from);
    let config = load_enterprise_config(config_path)?;
    let scenario = load_scenario_config(scenario_path)?;
    let report = EnterpriseEngine::new(config, scenario)?.run();
    write_or_print(&serde_json::to_value(report)?, output.as_deref())
}

fn protocol_fixture(args: &[String], protocol: Protocol) -> Result<(), Box<dyn Error>> {
    let (config_path, scenario_path) = config_paths(args);
    let request_path = option(args, "--request").ok_or("--request is required")?;
    let output = option(args, "--out").map(PathBuf::from);
    let request: Value = serde_json::from_str(&fs::read_to_string(request_path)?)?;
    let config = load_enterprise_config(config_path)?;
    let scenario = load_scenario_config(scenario_path)?;
    let mut engine = EnterpriseEngine::new(config, scenario)?;
    let response = match protocol {
        Protocol::Mcp => mcp::handle(&mut engine, &request),
        Protocol::A2a => a2a::handle(&mut engine, &request),
    };
    write_or_print(&response, output.as_deref())
}

fn protocol_stdio(args: &[String], protocol: Protocol) -> Result<(), Box<dyn Error>> {
    let (config_path, scenario_path) = config_paths(args);
    let config = load_enterprise_config(config_path)?;
    let scenario = load_scenario_config(scenario_path)?;
    let mut engine = EnterpriseEngine::new(config, scenario)?;
    let stdin = io::stdin();
    let mut stdout = io::stdout().lock();
    for line in stdin.lock().lines() {
        let line = line?;
        if line.trim().is_empty() {
            continue;
        }
        let response = match serde_json::from_str::<Value>(&line) {
            Ok(request) => match protocol {
                Protocol::Mcp => mcp::handle(&mut engine, &request),
                Protocol::A2a => a2a::handle(&mut engine, &request),
            },
            Err(error) => json!({
                "jsonrpc":"2.0",
                "id":Value::Null,
                "error":{
                    "code":-32700,
                    "message":"JSON_RPC_PARSE_ERROR",
                    "data":{"detail":error.to_string()}
                }
            }),
        };
        if response.is_null() {
            continue;
        }
        serde_json::to_writer(&mut stdout, &response)?;
        stdout.write_all(b"\n")?;
        stdout.flush()?;
    }
    Ok(())
}

fn self_test(args: &[String]) -> Result<(), Box<dyn Error>> {
    let (config_path, scenario_path) = config_paths(args);
    let config = load_enterprise_config(config_path)?;
    let scenario = load_scenario_config(scenario_path)?;
    let first = EnterpriseEngine::new(config.clone(), scenario.clone())?.run();
    let second = EnterpriseEngine::new(config.clone(), scenario.clone())?.run();
    let replay = compare_reports(&first, &second);

    let mut negative_engine = EnterpriseEngine::new(config.clone(), scenario.clone())?;
    let mut parameters = BTreeMap::new();
    parameters.insert("delta_pct".to_string(), "5".to_string());
    let budget_receipt = negative_engine.invoke_mcp_action(ActuationIntent {
        id: "negative-budget-authority".to_string(),
        action: "safe.budget.reallocate".to_string(),
        target: "lean-budget".to_string(),
        requested_by: "autonomic-budget-controller".to_string(),
        authority: "autonomic-budget-controller".to_string(),
        parameters,
    });

    let mcp_unknown = mcp::handle(
        &mut negative_engine,
        &json!({"jsonrpc":"2.0","id":41,"method":"unknown/method","params":{}}),
    );
    let a2a_unknown = a2a::handle(
        &mut negative_engine,
        &json!({
            "jsonrpc":"2.0",
            "id":42,
            "method":"message/send",
            "params":{
                "agent":"lean-portfolio-management-agent",
                "skill":"nonexistent-skill",
                "message":{"role":"user","parts":[{"kind":"text","text":"test refusal"}]}
            }
        }),
    );

    let checks = BTreeMap::from([
        (
            "deterministic_replay".to_string(),
            replay.values().all(|value| *value),
        ),
        (
            "simulation_alive".to_string(),
            first.standing == Standing::Alive,
        ),
        (
            "budget_human_boundary".to_string(),
            budget_receipt.code == "HUMAN_AUTHORIZATION_REQUIRED"
                && budget_receipt.decision == "REFUSED",
        ),
        (
            "mcp_unknown_method_typed".to_string(),
            mcp_unknown
                .pointer("/error/message")
                .and_then(Value::as_str)
                == Some("MCP_METHOD_NOT_FOUND"),
        ),
        (
            "a2a_unknown_skill_rejected".to_string(),
            a2a_unknown.pointer("/result/state").and_then(Value::as_str) == Some("rejected"),
        ),
    ]);
    let standing = if checks.values().all(|value| *value) {
        "ALIVE"
    } else {
        "BLOCKED"
    };
    let output = json!({
        "schema":"aps.safe-simulation-self-test.v26.7.30",
        "standing":standing,
        "checks":checks,
        "replay":replay,
        "firstReport":first,
        "negativeBudgetReceipt":budget_receipt,
        "mcpUnknown":mcp_unknown,
        "a2aUnknown":a2a_unknown
    });
    print_json(&output)?;
    if standing != "ALIVE" {
        return Err("self-test refused promotion".into());
    }
    Ok(())
}

fn config_paths(args: &[String]) -> (&Path, &Path) {
    let config = option(args, "--config").unwrap_or("config/fortune5-enterprise.json");
    let scenario = option(args, "--scenario").unwrap_or("config/global-core-modernization.json");
    (Path::new(config), Path::new(scenario))
}

fn option<'a>(args: &'a [String], name: &str) -> Option<&'a str> {
    args.windows(2)
        .find(|window| window[0] == name)
        .map(|window| window[1].as_str())
}

fn write_or_print(value: &Value, output: Option<&Path>) -> Result<(), Box<dyn Error>> {
    let text = serde_json::to_string_pretty(value)? + "\n";
    if let Some(path) = output {
        if let Some(parent) = path.parent() {
            fs::create_dir_all(parent)?;
        }
        fs::write(path, text)?;
    } else {
        print!("{text}");
    }
    Ok(())
}

fn print_json(value: &Value) -> Result<(), Box<dyn Error>> {
    let text = serde_json::to_string_pretty(value)?;
    println!("{text}");
    Ok(())
}

fn print_help() {
    println!(
        "aps-safe-sim\n\nCommands:\n  simulate --config <file> --scenario <file> [--out <file>]\n  mcp-fixture --config <file> --scenario <file> --request <file> [--out <file>]\n  a2a-fixture --config <file> --scenario <file> --request <file> [--out <file>]\n  mcp-stdio --config <file> --scenario <file>\n  a2a-jsonl --config <file> --scenario <file>\n  agent-cards\n  self-test --config <file> --scenario <file>"
    );
}

#[derive(Debug, Clone, Copy)]
enum Protocol {
    Mcp,
    A2a,
}

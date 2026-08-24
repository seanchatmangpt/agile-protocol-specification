use crate::engine::EnterpriseEngine;
use crate::model::{A2A_PROTOCOL_VERSION, A2aTask, A2aTaskState};
use serde::{Deserialize, Serialize};
use serde_json::{Value, json};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct AgentCapabilities {
    pub streaming: bool,
    pub push_notifications: bool,
    pub extended_agent_card: bool,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct AgentSkill {
    pub id: String,
    pub name: String,
    pub description: String,
    pub tags: Vec<String>,
    pub input_modes: Vec<String>,
    pub output_modes: Vec<String>,
}

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
#[serde(rename_all = "camelCase")]
pub struct AgentCard {
    pub protocol_version: String,
    pub name: String,
    pub description: String,
    pub url: String,
    pub version: String,
    pub capabilities: AgentCapabilities,
    pub default_input_modes: Vec<String>,
    pub default_output_modes: Vec<String>,
    pub skills: Vec<AgentSkill>,
}

pub fn handle(engine: &mut EnterpriseEngine, request: &Value) -> Value {
    let id = request.get("id").cloned().unwrap_or(Value::Null);
    let method = match request.get("method").and_then(Value::as_str) {
        Some(method) => method,
        None => return error(id, -32600, "A2A_INVALID_REQUEST", None),
    };
    match method {
        "agent/getCard" => get_card(id, request),
        "message/send" => send_message(engine, id, request),
        "tasks/get" => get_task(engine, id, request),
        "tasks/list" => list_tasks(engine, id),
        "tasks/cancel" => cancel_task(engine, id, request),
        _ => error(
            id,
            -32601,
            "A2A_METHOD_NOT_FOUND",
            Some(json!({"method": method})),
        ),
    }
}

pub fn agent_cards() -> Vec<AgentCard> {
    vec![
        card(
            "lean-portfolio-management-agent",
            "Lean Portfolio Management Agent",
            "Coordinates portfolio strategy, guardrails, and PI intent without owning execution tools",
            vec![skill(
                "plan-pi",
                "Plan PI",
                "Creates a bounded cross-portfolio PI plan artifact",
                &["portfolio", "planning", "safe"],
            )],
        ),
        card(
            "solution-train-coordination-agent",
            "Solution Train Coordination Agent",
            "Coordinates cross-ART dependencies and delegates bounded capacity actions through MCP",
            vec![skill(
                "resolve-dependency",
                "Resolve Dependency",
                "Requests a receipted capacity rebalance through the MCP actuation plane",
                &["solution-train", "dependency", "flow"],
            )],
        ),
        card(
            "enterprise-architecture-agent",
            "Enterprise Architecture Agent",
            "Evaluates architecture runway and system-of-systems risk",
            vec![skill(
                "review-architecture",
                "Review Architecture",
                "Produces an architecture runway observation artifact",
                &["architecture", "runway", "enabler"],
            )],
        ),
        card(
            "release-governance-agent",
            "Release Governance Agent",
            "Evaluates exact release candidates against compliance, flow, and receipt evidence",
            vec![skill(
                "evaluate-release",
                "Evaluate Release",
                "Calls the MCP release gate and returns the resulting artifact",
                &["release", "governance", "compliance"],
            )],
        ),
        card(
            "investment-committee-agent",
            "Investment Committee Liaison Agent",
            "Collects budget evidence but cannot impersonate human investment authority",
            vec![skill(
                "authorize-budget",
                "Request Budget Authorization",
                "Transitions to input-required rather than autonomously changing lean budgets",
                &["budget", "human-in-the-loop", "governance"],
            )],
        ),
    ]
}

fn get_card(id: Value, request: &Value) -> Value {
    let name = request
        .pointer("/params/name")
        .and_then(Value::as_str)
        .unwrap_or_default();
    match agent_cards().into_iter().find(|card| card.name == name) {
        Some(card) => success(
            id,
            serde_json::to_value(card).expect("card serialization must succeed"),
        ),
        None => error(
            id,
            -32004,
            "A2A_AGENT_CARD_NOT_FOUND",
            Some(json!({"name": name})),
        ),
    }
}

fn send_message(engine: &mut EnterpriseEngine, id: Value, request: &Value) -> Value {
    let agent = request
        .pointer("/params/agent")
        .and_then(Value::as_str)
        .unwrap_or_default();
    let skill = request
        .pointer("/params/skill")
        .and_then(Value::as_str)
        .unwrap_or_default();
    let text = request
        .pointer("/params/message/parts/0/text")
        .and_then(Value::as_str)
        .unwrap_or_default();
    if agent.is_empty() || skill.is_empty() || text.is_empty() {
        return error(id, -32602, "A2A_MESSAGE_PARAMS_INVALID", None);
    }
    let task = engine.submit_a2a_task(agent, skill, text);
    success(
        id,
        serde_json::to_value(task).expect("task serialization must succeed"),
    )
}

fn get_task(engine: &EnterpriseEngine, id: Value, request: &Value) -> Value {
    let task_id = request
        .pointer("/params/id")
        .and_then(Value::as_str)
        .unwrap_or_default();
    match engine.task(task_id) {
        Some(task) => success(
            id,
            serde_json::to_value(task).expect("task serialization must succeed"),
        ),
        None => error(
            id,
            -32001,
            "A2A_TASK_NOT_FOUND",
            Some(json!({"id": task_id})),
        ),
    }
}

fn list_tasks(engine: &EnterpriseEngine, id: Value) -> Value {
    let tasks = engine
        .tasks()
        .into_iter()
        .cloned()
        .collect::<Vec<A2aTask>>();
    success(id, json!({"tasks": tasks}))
}

fn cancel_task(engine: &mut EnterpriseEngine, id: Value, request: &Value) -> Value {
    let task_id = request
        .pointer("/params/id")
        .and_then(Value::as_str)
        .unwrap_or_default();
    match engine.cancel_task(task_id) {
        Ok(task) => success(
            id,
            serde_json::to_value(task).expect("task serialization must succeed"),
        ),
        Err(code) => error(id, -32002, &code, Some(json!({"id": task_id}))),
    }
}

fn card(name: &str, _title: &str, description: &str, skills: Vec<AgentSkill>) -> AgentCard {
    AgentCard {
        protocol_version: A2A_PROTOCOL_VERSION.to_string(),
        name: name.to_string(),
        description: description.to_string(),
        url: format!("https://simulation.invalid/a2a/{name}"),
        version: "26.7.30".to_string(),
        capabilities: AgentCapabilities {
            streaming: false,
            push_notifications: false,
            extended_agent_card: false,
        },
        default_input_modes: vec!["text/plain".to_string(), "application/json".to_string()],
        default_output_modes: vec!["application/json".to_string()],
        skills,
    }
}

fn skill(id: &str, name: &str, description: &str, tags: &[&str]) -> AgentSkill {
    AgentSkill {
        id: id.to_string(),
        name: name.to_string(),
        description: description.to_string(),
        tags: tags.iter().map(|tag| (*tag).to_string()).collect(),
        input_modes: vec!["text/plain".to_string(), "application/json".to_string()],
        output_modes: vec!["application/json".to_string()],
    }
}

fn success(id: Value, result: Value) -> Value {
    json!({"jsonrpc":"2.0","id":id,"result":result})
}

fn error(id: Value, code: i64, message: &str, data: Option<Value>) -> Value {
    let mut body = json!({"code":code,"message":message});
    if let Some(data) = data {
        body["data"] = data;
    }
    json!({"jsonrpc":"2.0","id":id,"error":body})
}

pub fn is_terminal(state: &A2aTaskState) -> bool {
    matches!(
        state,
        A2aTaskState::Completed
            | A2aTaskState::Canceled
            | A2aTaskState::Failed
            | A2aTaskState::Rejected
    )
}

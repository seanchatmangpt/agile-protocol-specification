use crate::broker::ActuationIntent;
use crate::engine::EnterpriseEngine;
use crate::model::MCP_PROTOCOL_VERSION;
use serde_json::{Value, json};
use std::collections::BTreeMap;

pub fn handle(engine: &mut EnterpriseEngine, request: &Value) -> Value {
    let id = request.get("id").cloned().unwrap_or(Value::Null);
    let method = match request.get("method").and_then(Value::as_str) {
        Some(method) => method,
        None => return error(id, -32600, "MCP_INVALID_REQUEST", None),
    };
    match method {
        "initialize" => initialize(id, request),
        "notifications/initialized" => Value::Null,
        "tools/list" => success(id, json!({"tools": tool_definitions()})),
        "tools/call" => call_tool(engine, id, request),
        "resources/list" => success(id, json!({"resources": resource_definitions()})),
        "resources/read" => read_resource(engine, id, request),
        "prompts/list" => success(id, json!({"prompts": prompt_definitions()})),
        "prompts/get" => get_prompt(id, request),
        _ => error(
            id,
            -32601,
            "MCP_METHOD_NOT_FOUND",
            Some(json!({"method": method})),
        ),
    }
}

fn initialize(id: Value, request: &Value) -> Value {
    let requested = request
        .pointer("/params/protocolVersion")
        .and_then(Value::as_str)
        .unwrap_or_default();
    if requested != MCP_PROTOCOL_VERSION {
        return error(
            id,
            -32602,
            "MCP_PROTOCOL_VERSION_UNSUPPORTED",
            Some(json!({
                "requested": requested,
                "supported": MCP_PROTOCOL_VERSION
            })),
        );
    }
    success(
        id,
        json!({
            "protocolVersion": MCP_PROTOCOL_VERSION,
            "capabilities": {
                "logging": {},
                "prompts": {"listChanged": false},
                "resources": {"subscribe": false, "listChanged": false},
                "tools": {"listChanged": false}
            },
            "serverInfo": {
                "name": "aps-fortune5-safe-sim",
                "title": "APS Fortune-5-Scale SAFe Simulation",
                "version": "26.7.30",
                "description": "Deterministic MCP tool and resource surface for a simulated enterprise"
            }
        }),
    )
}

fn call_tool(engine: &mut EnterpriseEngine, id: Value, request: &Value) -> Value {
    let name = request
        .pointer("/params/name")
        .and_then(Value::as_str)
        .unwrap_or_default();
    let arguments = request
        .pointer("/params/arguments")
        .and_then(Value::as_object)
        .cloned()
        .unwrap_or_default();
    match name {
        "safe.enterprise.inspect" => success(
            id,
            tool_result(
                false,
                json!({
                    "enterprise": &engine.config.name,
                    "scale": &engine.scale,
                    "topologyDigest": topology_digest(&engine.topology),
                    "metrics": &engine.metrics,
                    "receiptHead": engine.ledger.head()
                }),
            ),
        ),
        "safe.receipts.head" => success(
            id,
            tool_result(
                false,
                json!({
                    "head": engine.ledger.head(),
                    "entries": engine.ledger.entries().len(),
                    "chainValid": engine.ledger.verify()
                }),
            ),
        ),
        "safe.portfolio.freeze-intake"
        | "safe.portfolio.unfreeze-intake"
        | "safe.capacity.rebalance"
        | "safe.architecture.allocate-enabler"
        | "safe.release.evaluate"
        | "safe.budget.reallocate" => {
            let authority = arguments
                .get("authority")
                .and_then(Value::as_str)
                .unwrap_or("mcp-unauthorized-client")
                .to_string();
            let target = arguments
                .get("target")
                .and_then(Value::as_str)
                .unwrap_or("enterprise")
                .to_string();
            let mut parameters = BTreeMap::new();
            for (key, value) in arguments {
                if key == "authority" || key == "target" {
                    continue;
                }
                parameters.insert(key, scalar_string(&value));
            }
            let method_token = name.replace('.', "-");
            let sequence = engine.ledger.entries().len() + 1;
            let receipt = engine.invoke_mcp_action(ActuationIntent {
                id: format!("mcp-{method_token}-{sequence}"),
                action: name.to_string(),
                target,
                requested_by: "mcp-client".to_string(),
                authority,
                parameters,
            });
            let is_error = receipt.decision != "APPLIED";
            success(
                id,
                tool_result(
                    is_error,
                    serde_json::to_value(receipt).expect("receipt serialization must succeed"),
                ),
            )
        }
        _ => success(
            id,
            tool_result(
                true,
                json!({
                    "standing": "UNSUPPORTED",
                    "code": "MCP_TOOL_UNSUPPORTED",
                    "tool": name
                }),
            ),
        ),
    }
}

fn read_resource(engine: &EnterpriseEngine, id: Value, request: &Value) -> Value {
    let uri = request
        .pointer("/params/uri")
        .and_then(Value::as_str)
        .unwrap_or_default();
    let value = match uri {
        "aps://enterprise/topology" => json!({
            "enterprise": &engine.config.name,
            "scale": &engine.scale,
            "topologyDigest": topology_digest(&engine.topology),
            "topology": &engine.topology,
            "configuration": &engine.config
        }),
        "aps://safe/metrics" => json!({"metrics": &engine.metrics}),
        "aps://safe/a2a-agent-cards" => json!({"agents": crate::a2a::agent_cards()}),
        "aps://evidence/receipt-head" => json!({
            "head": engine.ledger.head(),
            "entries": engine.ledger.entries().len(),
            "chainValid": engine.ledger.verify()
        }),
        _ => {
            return error(
                id,
                -32002,
                "MCP_RESOURCE_NOT_FOUND",
                Some(json!({"uri": uri})),
            );
        }
    };
    success(
        id,
        json!({
            "contents": [{
                "uri": uri,
                "mimeType": "application/json",
                "text": serde_json::to_string_pretty(&value).expect("resource serialization must succeed")
            }]
        }),
    )
}

fn get_prompt(id: Value, request: &Value) -> Value {
    let name = request
        .pointer("/params/name")
        .and_then(Value::as_str)
        .unwrap_or_default();
    let text = match name {
        "safe.pi-planning" => {
            "Construct a bounded PI plan. Identify cross-ART dependencies, capacity guardrails, architecture runway, compliance evidence, and same-object falsifiers."
        }
        "safe.inspect-and-adapt" => {
            "Review flow, quality, predictability, dependency age, budget consumption, and refusal receipts. Propose only bounded changes through the actuation broker."
        }
        "safe.release-governance" => {
            "Evaluate the exact release candidate coordinate. Do not infer readiness from schedule or tracker state. Require compliance, flow, receipt, and replay evidence."
        }
        _ => {
            return error(
                id,
                -32602,
                "MCP_PROMPT_NOT_FOUND",
                Some(json!({"name": name})),
            );
        }
    };
    success(
        id,
        json!({
            "description": format!("APS prompt profile: {name}"),
            "messages": [{
                "role": "user",
                "content": {"type": "text", "text": text}
            }]
        }),
    )
}

fn tool_result(is_error: bool, structured: Value) -> Value {
    json!({
        "content": [{
            "type": "text",
            "text": serde_json::to_string(&structured).expect("tool result serialization must succeed")
        }],
        "structuredContent": structured,
        "isError": is_error
    })
}

fn tool_definitions() -> Vec<Value> {
    vec![
        tool(
            "safe.enterprise.inspect",
            "Inspect the admitted enterprise topology and current flow metrics",
            json!({"type":"object","additionalProperties":false}),
        ),
        tool(
            "safe.portfolio.freeze-intake",
            "Freeze portfolio intake when WIP exceeds the admitted guardrail",
            authority_schema(),
        ),
        tool(
            "safe.portfolio.unfreeze-intake",
            "Unfreeze portfolio intake after WIP returns below the release threshold",
            authority_schema(),
        ),
        tool(
            "safe.capacity.rebalance",
            "Move at most five percent capacity to resolve cross-ART dependencies",
            json!({
                "type":"object",
                "additionalProperties":false,
                "required":["authority","delta_pct"],
                "properties":{
                    "authority":{"type":"string"},
                    "target":{"type":"string"},
                    "delta_pct":{"type":"integer","minimum":1,"maximum":5}
                }
            }),
        ),
        tool(
            "safe.architecture.allocate-enabler",
            "Allocate bounded enabler capacity to architecture runway",
            json!({
                "type":"object",
                "additionalProperties":false,
                "required":["authority","target_pct"],
                "properties":{
                    "authority":{"type":"string"},
                    "target":{"type":"string"},
                    "target_pct":{"type":"integer","minimum":1,"maximum":25}
                }
            }),
        ),
        tool(
            "safe.release.evaluate",
            "Evaluate a release candidate without bypassing compliance or flow gates",
            authority_schema(),
        ),
        tool(
            "safe.budget.reallocate",
            "Request lean-budget reallocation; autonomous callers are refused",
            json!({
                "type":"object",
                "additionalProperties":false,
                "required":["authority","delta_pct"],
                "properties":{
                    "authority":{"type":"string"},
                    "target":{"type":"string"},
                    "delta_pct":{"type":"integer","minimum":1,"maximum":10}
                }
            }),
        ),
        tool(
            "safe.receipts.head",
            "Read the current receipt-chain head",
            json!({"type":"object","additionalProperties":false}),
        ),
    ]
}

fn resource_definitions() -> Vec<Value> {
    vec![
        resource(
            "aps://enterprise/topology",
            "Enterprise topology",
            "Fortune-5-scale simulated SAFe topology",
        ),
        resource(
            "aps://safe/metrics",
            "SAFe flow metrics",
            "Current deterministic simulation metrics",
        ),
        resource(
            "aps://safe/a2a-agent-cards",
            "A2A agent cards",
            "Discoverable peer-agent capabilities",
        ),
        resource(
            "aps://evidence/receipt-head",
            "Receipt ledger head",
            "Current hash-chain coordinate",
        ),
    ]
}

fn prompt_definitions() -> Vec<Value> {
    vec![
        json!({"name":"safe.pi-planning","title":"PI Planning","description":"Construct a bounded enterprise PI plan","arguments":[]}),
        json!({"name":"safe.inspect-and-adapt","title":"Inspect and Adapt","description":"Diagnose flow and evidence without direct actuation","arguments":[]}),
        json!({"name":"safe.release-governance","title":"Release Governance","description":"Evaluate a release candidate at an exact coordinate","arguments":[]}),
    ]
}

fn tool(name: &str, description: &str, input_schema: Value) -> Value {
    json!({
        "name": name,
        "title": name,
        "description": description,
        "inputSchema": input_schema,
        "outputSchema": {
            "type":"object"
        }
    })
}

fn authority_schema() -> Value {
    json!({
        "type":"object",
        "additionalProperties":false,
        "required":["authority"],
        "properties":{
            "authority":{"type":"string"},
            "target":{"type":"string"}
        }
    })
}

fn resource(uri: &str, name: &str, description: &str) -> Value {
    json!({
        "uri": uri,
        "name": name,
        "description": description,
        "mimeType": "application/json"
    })
}

fn topology_digest(topology: &crate::model::EnterpriseTopology) -> String {
    use sha2::{Digest, Sha256};
    let bytes = serde_json::to_vec(topology).expect("topology serialization must succeed");
    Sha256::digest(bytes)
        .iter()
        .map(|byte| format!("{byte:02x}"))
        .collect()
}

fn scalar_string(value: &Value) -> String {
    match value {
        Value::String(value) => value.clone(),
        Value::Number(value) => value.to_string(),
        Value::Bool(value) => value.to_string(),
        _ => value.to_string(),
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

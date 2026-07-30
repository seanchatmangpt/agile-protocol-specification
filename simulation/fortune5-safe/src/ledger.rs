use crate::model::Event;
use serde::{Deserialize, Serialize};
use sha2::{Digest, Sha256};

#[derive(Debug, Clone, Serialize, Deserialize, PartialEq, Eq)]
pub struct LedgerEntry {
    pub sequence: u64,
    pub previous_hash: String,
    pub hash: String,
    pub event: Event,
}

#[derive(Debug, Clone, Default)]
pub struct ReceiptLedger {
    entries: Vec<LedgerEntry>,
    head: String,
}

impl ReceiptLedger {
    pub fn new() -> Self {
        Self {
            entries: Vec::new(),
            head: "0".repeat(64),
        }
    }

    pub fn append(&mut self, mut event: Event) -> String {
        let sequence = self.entries.len() as u64 + 1;
        event.sequence = sequence;
        let previous_hash = self.head.clone();
        let encoded = serde_json::to_vec(&event).expect("event serialization must succeed");
        let mut hasher = Sha256::new();
        hasher.update(previous_hash.as_bytes());
        hasher.update(encoded);
        let hash = encode_hex(&hasher.finalize());
        self.entries.push(LedgerEntry {
            sequence,
            previous_hash,
            hash: hash.clone(),
            event,
        });
        self.head = hash.clone();
        hash
    }

    pub fn head(&self) -> &str {
        &self.head
    }

    pub fn entries(&self) -> &[LedgerEntry] {
        &self.entries
    }

    pub fn verify(&self) -> bool {
        let mut previous_hash = "0".repeat(64);
        for (index, entry) in self.entries.iter().enumerate() {
            if entry.sequence != index as u64 + 1 || entry.previous_hash != previous_hash {
                return false;
            }
            let encoded = match serde_json::to_vec(&entry.event) {
                Ok(value) => value,
                Err(_) => return false,
            };
            let mut hasher = Sha256::new();
            hasher.update(previous_hash.as_bytes());
            hasher.update(encoded);
            let expected = encode_hex(&hasher.finalize());
            if expected != entry.hash {
                return false;
            }
            previous_hash = entry.hash.clone();
        }
        previous_hash == self.head
    }
}

fn encode_hex(bytes: &[u8]) -> String {
    let mut output = String::with_capacity(bytes.len() * 2);
    for byte in bytes {
        use std::fmt::Write as _;
        write!(&mut output, "{byte:02x}").expect("writing to String cannot fail");
    }
    output
}

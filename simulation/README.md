# APS v26.8.24 Simulations

Active simulations are executable falsifiers and sensitivity experiments, not product demos.

The predecessor Fortune-5 SAFe/MCP/A2A Rust simulation is archived by immutable predecessor commit and is no longer active authority because it tests the prior APS object model.

The current synthetic enterprise experiment is driven by:

- `examples/fortune500-fibo/enterprise.json`
- `examples/fortune500-fibo/knowledge-contract.json`
- `examples/fortune500-fibo/reconstitution.json`
- `examples/fortune500-fibo/process-events.json`
- `tools/simulate_fortune500.py`

Run:

```bash
python3 tools/simulate_fortune500.py examples/fortune500-fibo/enterprise.json
```

The simulation is deterministic arithmetic over explicit assumptions. It is useful for sensitivity analysis of candidate-space breadth, generated surface volume, full human lifecycle-equivalent effort, and governance compression. It is not empirical evidence about a real Fortune-500 company.

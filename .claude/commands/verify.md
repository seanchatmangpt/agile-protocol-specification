# /verify

Run the full APS qualification program:

```bash
python3 tools/verify.py --no-receipt
python3 -m unittest discover -s tests -v
mdbook build -d /tmp/aps-book specification-guide
python3 tools/simulate_fortune500.py examples/fortune500-fibo/enterprise.json --receipt /tmp/aps-simulation.json
```

Report exact standing and do not upgrade failures into narrative success.

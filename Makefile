.PHONY: verify test book simulate all

verify:
	python3 tools/verify.py --no-receipt

test:
	python3 -m unittest discover -s tests -v

book:
	mdbook build -d /tmp/aps-book specification-guide

simulate:
	python3 tools/simulate_fortune500.py examples/fortune500-fibo/enterprise.json

all: verify test book simulate

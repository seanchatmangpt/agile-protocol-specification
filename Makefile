.PHONY: deps verify test book simulate all

deps:
	python3 -m pip install --disable-pip-version-check -r tools/requirements-ci.txt

verify:
	python3 tools/verify.py --no-receipt

test:
	python3 -m unittest discover -s tests -v

book:
	mdbook build -d /tmp/aps-book specification-guide

simulate:
	python3 tools/simulate_fortune500.py examples/fortune500-fibo/enterprise.json

all: deps verify test book simulate

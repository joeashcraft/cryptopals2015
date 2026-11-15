.PHONY: test coverage annotate clean-coverage help

PYTHON ?= python
COVERAGE ?= coverage
COV_DIR := coverage

# unittest discover only accepts one -p at a time; run both naming styles.
TEST_PATTERNS := test*.py *test.py

help:
	@echo "Targets:"
	@echo "  make test       - run unittest for test*.py and *test.py"
	@echo "  make coverage   - run tests under coverage and print report"
	@echo "  make annotate   - coverage report + annotated sources in $(COV_DIR)/"
	@echo "  make clean-coverage - remove .coverage and $(COV_DIR)/"

test:
	@for pattern in $(TEST_PATTERNS); do \
		echo "==> unittest discover -p '$$pattern'"; \
		$(PYTHON) -m unittest discover -v -p "$$pattern" || exit 1; \
	done

coverage:
	rm -f .coverage
	@for pattern in $(TEST_PATTERNS); do \
		echo "==> coverage run -a -m unittest discover -p '$$pattern'"; \
		$(COVERAGE) run -a -m unittest discover -p "$$pattern" || exit 1; \
	done
	$(COVERAGE) report -m

annotate: coverage
	mkdir -p $(COV_DIR)
	$(COVERAGE) annotate -d $(COV_DIR)/

clean-coverage:
	rm -f .coverage
	rm -rf $(COV_DIR)

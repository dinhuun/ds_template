# set default goal to 'help' so nothing runs by accident
.DEFAULT_GOAL := help

.PHONY: clean help install lint sync test test_integration test_unit

## build project into wheel and sdist
build: clean
	@echo "building distribution archives..."
	uv build
	@echo "build complete. Artifacts are in the dist/ directory"

## remove build artifacts, cache artifacts, compiled files
clean:
	@echo "cleaning up build artifacts, compiled files, cache artifacts..."
	@find . -type f -name "*.py[co]" -delete -o -type d -name "__pycache__" -delete
	@rm -rf .ruff_cache .ty_cache .pytest_cache .uv_cache .coverage dist build *.egg-info
	@echo "clean complete"

## show this help message
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-19s\033[0m %s\n", $$1, $$2}'

## install environment
install: sync

## lint
lint:
	uv run ruff check --fix src tests
	uv run ruff format src tests
	uv run ty check src tests

## sync environment
sync:
	@echo "syncing environments..."
	uv sync
	@echo "synced environment. Use 'uv run <command>' to execute."

## test all
test:
	uv run pytest tests/unit/ tests/integration/

# test integration
test_integration:
	uv run pytest tests/integration/

## test unit
test_unit:
	uv run pytest tests/unit/

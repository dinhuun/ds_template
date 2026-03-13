.PHONY: clean help install lint sync test

# set default goal to 'help' so nothing runs by accident
.DEFAULT_GOAL := help

## remove build artifacts, cache artifacts, compiled files
clean:
	@echo "cleaning up build artifacts, compiled files, cache artifacts..."
	@find . -type f -name "*.py[co]" -delete -o -type d -name "__pycache__" -delete
	@rm -rf .ruff_cache .ty_cache .pytest_cache .uv_cache .coverage dist build *.egg-info
	@echo "clean complete"

## sync environment
install: sync
sync:
	@echo "syncing environments..."
	uv sync
	@echo "synced environment. Use 'uv run <command>' to execute."

## lint
lint:
	uv run ruff check --fix tests
	uv run ruff format tests
	uv run ty check tests

## test
test:
	uv run pytest tests/unit/

## show this help message
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-19s\033[0m %s\n", $$1, $$2}'

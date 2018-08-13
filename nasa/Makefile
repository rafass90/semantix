

help:  ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | sort
# VARIABLES ARGUMENTS

message=auto generate

export PYTHONDONTWRITEBYTECODE=1
export SPARK_LOCAL_IP=localhost

.PHONY: help

clean: ## Clean local environment
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf

dependencies: ## Install development dependencies
	pip install -U -r requirements.txt

run: ## Run application server
	python nasa.py

shell: ## Open shell
	ipython

lint: ## Run code lint
	flake8 --show-source .
	isort --check

fix-python-import: ## Organize python imports
	isort -rc .
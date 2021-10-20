build:
	@echo "--> Building Docker DEV Image"
	docker build -t request_logging .

bash:
	@echo "--> Starting a bash interactor."
	docker run -v $(PWD)/:/code -it request_logging bash

test: ## Run all tests.
	@echo "--> Testing."
	docker run -v $(PWD)/:/code request_logging bash -c "python load_test.py"

clean:
	@find . -name "*.pyc" -exec rm -rf {} \;
	@find . -name "__pycache__" -delete

run-tests:
	@echo 'Running tests...'
	pytest -v --color=yes

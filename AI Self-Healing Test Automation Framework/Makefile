# Makefile for WhatsApp AI Automation Framework

.PHONY: help install install-dev venv run-tests test test-verbose test-coverage lint format clean

help:
	@echo "WhatsApp AI Automation Framework - Available Commands"
	@echo "=====================================================\n"
	@echo "setup commands:"
	@echo "  make venv          - Create virtual environment"
	@echo "  make install       - Install dependencies"
	@echo "  make install-dev   - Install with dev dependencies\n"
	@echo "testing commands:"
	@echo "  make test          - Run all tests"
	@echo "  make test-verbose  - Run tests with verbose output"
	@echo "  make test-coverage - Run tests with coverage report\n"
	@echo "code quality commands:"
	@echo "  make lint          - Run pylint"
	@echo "  make format        - Format code with black\n"
	@echo "utility commands:"
	@echo "  make clean         - Remove generated files"
	@echo "  make help          - Show this help message"

venv:
	python -m venv venv
	@echo "Virtual environment created. Activate with:"
	@echo "  source venv/bin/activate (Linux/Mac)"
	@echo "  venv\\Scripts\\activate (Windows)"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install pytest-cov pytest-xdist pytest-html pylint black

test:
	pytest tests/ -v

test-verbose:
	pytest tests/ -vv -s

test-coverage:
	pytest tests/ --cov=. --cov-report=html --cov-report=term

test-html:
	pytest tests/ -v --html=reports/report.html --self-contained-html

lint:
	pylint --disable=all --enable=E,F $(shell find . -name "*.py" -type f ! -path "./venv/*")

format:
	black . --exclude venv

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info

run-tests: test-html
	@echo "Test report generated at reports/report.html"

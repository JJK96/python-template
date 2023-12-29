.PHONY: tests install run

run:
	python -m {{cookiecutter.package_name}} --help

install:
	pip install -e .

tests:
	python -m pytest tests --cov=./{{cookiecutter.package_name}}

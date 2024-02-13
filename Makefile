SHELL := bash

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of: "
	@echo ""
	@echo "  install     install packages and prepare environment"
	@echo "  clean       remove all temporary files"
	@echo "  lint        run the code linters"
	@echo "  format      reformat code"
	@echo "  test        run all the tests"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

.PHONY: test
test: $(INSTALL_STAMP)
	$(POETRY) run pytest ./tests/ --cov-report term-missing --cov-fail-under 100 --cov $(NAME)

.PHONY: install
install:
	poetry install

.PHONY: runserver
runserver:
	poetry run python manage.py runserver

.PHONY: createsuperuser
createsuperuser:
	poetry run python manage.py createsuperuser

.PHONY: migrate
migrate:
	poetry run python manage.py migrate

.PHONY: makemigrations
makemigrations:
	poetry run python manage.py makemigrations

.PHONY: update
update: install migrate ;

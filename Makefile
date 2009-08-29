PROJECT_NAME = qqmls
SHELL := /bin/sh
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  all                      to setup the whole production environment for the project"
	@echo "  dev                      to setup the whole development environment for the project"
	@echo "  virtualenv               to create the virtualenv for the project"
	@echo "  requirements             install the requirements to the virtualenv"
	@echo "  db                       create the PostgreSQL db for the project"
	@echo "  migrate                  run the migrations"
	@echo "  runserver                Start the django dev server"
	@echo "  superuser                Create superuser with name superuser and password pass"

.PHONY: requirements

all: virtualenv requirements_prod migrate update_static superuser

dev: virtualenv requirements_dev db migrate superuser

# Command variables
MANAGE_CMD = python manage.py
PIP_INSTALL_CMD = pip install
VIRTUALENV_NAME = venv

# The default server host local development
HOST ?= localhost:8000


virtualenv:
	( \
		rm -rf venv; \
		virtualenv $(VIRTUALENV_NAME); \
	)

requirements_dev:
	( \
		. $(VIRTUALENV_NAME)/bin/activate; \
		$(PIP_INSTALL_CMD) -r requirements_dev.txt; \
	)

requirements_prod:
	( \
		. $(VIRTUALENV_NAME)/bin/activate; \
		$(PIP_INSTALL_CMD) -r requirements.txt; \
	)

db:
	( \
		dropdb enterday; \
		createdb enterday; \
	)

migrate:
	( \
		. $(VIRTUALENV_NAME)/bin/activate; \
		$(MANAGE_CMD) migrate; \
	)

superuser:
	( \
		. $(VIRTUALENV_NAME)/bin/activate; \
		$(MANAGE_CMD) createsuperuser; \
	)

runserver:
	( \
		. $(VIRTUALENV_NAME)/bin/activate; \
		$(MANAGE_CMD) runserver $(HOST); \
	)

update_static:
	# update static
	( \
		. $(VIRTUALENV_NAME)/bin/activate; \
		$(MANAGE_CMD) collectstatic; \
	)

clean:
	# Remove files not in source control
	find . -type f -name "*.pyc" -delete

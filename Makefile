APP=gcp-infra-helper

VERSION =? $(shell git branch | sed -n -e 's/^\* \(.*\)/\1/p')

PYTHON ?= $(shell which python3.8)

GCP_PROJECT ?= ""

.PHONY: clean

setup:
	[ ! -d venv ] && $(PYTHON) -m venv venv  && source venv/bin/activate && python -m pip install -U pip && pip install --no-cache-dir -r requirements.txt
	@echo -------------------------
	@echo To start your python environement use:
	@echo  . /venv/bin/activate 
	@echo -------------------------

update-requirements:
	$(PYTHON) -m pip freeze >requirements.txt

build-clean:
	rm dist/*

build-module:
	$(PYTHON) -m build


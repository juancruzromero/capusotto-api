SHELL=/bin/bash
PYTHON=python
MAIN=manage.py
ARGS=$(filter-out $@,$(MAKECMDGOALS))

# Atajos para ejecutar proyecto -> make app <subcommand>
# Ejemplo: make app runserver
app: $(MAIN)
	python $(MAIN) $(word 1,$(ARGS))
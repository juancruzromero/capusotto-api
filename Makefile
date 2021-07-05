SHELL=/bin/bash
PYTHON=python
MAIN=manage.py
ARGS=$(filter-out $@,$(MAKECMDGOALS))

# Runserver -> Ejemplo: make run
run: $(MAIN)
	python $(MAIN) runserver

# Atajos para ejecutar proyecto -> make app <subcommand>
# Ejemplo: make app makemigrations
app: $(MAIN)
	python $(MAIN) $(word 1,$(ARGS))
PYTHON      := uv run python
SRC_DIR     := src

.PHONY: install run debug clean lint lint-strict

install:
	uv sync

run:
	$(PYTHON) -m $(SRC_DIR)

debug:
	uv run python -m pdb -m $(SRC_DIR)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +

lint:
	$(PYTHON) -m flake8 $(SRC_DIR)
	$(PYTHON) -m mypy $(SRC_DIR) --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	$(PYTHON) -m flake8 $(SRC_DIR)
	$(PYTHON) -m mypy $(SRC_DIR) --strict

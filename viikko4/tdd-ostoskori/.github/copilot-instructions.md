# Copilot instructions

## Build and test

Python 3.14 project using `uv` and `uv.lock`. Run commands from the
`viikko4/tdd-ostoskori` directory.

```bash
# Create/update the project environment from pyproject.toml and uv.lock
uv sync

# Run the full test suite
uv run pytest

# Run the cart test module
uv run pytest src/tests/ostoskori_test.py

# Run one test by node id
uv run pytest src/tests/ostoskori_test.py::TestOstoskori::test_ostoskorin_hinta_ja_tavaroiden_maara_alussa
```

Tests use pytest with `unittest.TestCase` and `setUp`. No lint task is
configured.

## Architecture

The code models a shopping cart with these domain classes:

- `Tuote`: product name, unit price, and currently unused stock field.
- `Ostos`: cart line with quantity starting at one, non-negative quantity, and
  line-total calculation.
- `Ostoskori`: adds/removes products, clears the cart, reports item count and
  total price, and exposes cart lines.
- `src/index.py`: placeholder; behavior lives in the domain classes and tests.

Source files are flat modules under `src/`, not an installed package hierarchy.
Tests import modules such as `ostoskori` and `tuote` directly; preserve this
layout and run pytest from the project root.

## Repository conventions

- Use the existing Finnish domain vocabulary for public names
  (`Ostoskori`, `Ostos`, `Tuote`, `hinta`, `lisaa_tuote`, etc.).
- Prices are integers; `Ostos.hinta()` is quantity multiplied by product price.
- Cart behavior is developed incrementally in `src/tests/ostoskori_test.py`;
  extend its `unittest.TestCase` pattern and use `setUp` for a fresh cart.

## Other
- Tests executed with uv run pytest
- Code of ostos.py and tuote.py should not be changed
- Tests should not be edited unless explicitly asked
- Always implement absolutely minimal code that makes the tests pass


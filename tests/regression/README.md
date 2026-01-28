# Regression Tests

This directory contains end-to-end regression tests that simulate real client behavior.

## Purpose

Regression tests verify complete workflows:
- Frontend → Backend interactions
- Full user journeys
- Integration between components
- Real-world scenarios

## Running Regression Tests

```bash
pytest tests/regression/ --maxfail=1 --exitfirst -v
```

Or use VS Code: **[TEST][REGRESSION] Full regression suite**

## Prerequisites

Some regression tests may require:
- Backend server running (or use test client)
- Test data files
- Environment variables configured

## Configuration

- **Fail-fast**: Enabled (`--maxfail=1 --exitfirst`)
- **Timeout**: 30 seconds per test (default)
- **Deterministic**: All tests exit cleanly

## Writing Regression Tests

Regression tests should:
- **Simulate real usage** - Mimic actual user behavior
- **Test complete flows** - From start to finish
- **Use realistic data** - Real-world examples
- **Verify end-to-end** - Check the entire pipeline

## Example

See `test_regression_example.py` for a basic regression test template.

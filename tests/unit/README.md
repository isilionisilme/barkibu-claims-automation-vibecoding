# Unit Tests

This directory contains unit tests for individual components and functions.

## Purpose

Unit tests verify that individual components work correctly in isolation:
- Backend API endpoints
- Data processing functions
- Utility functions
- Frontend components (when applicable)

## Running Unit Tests

```bash
pytest tests/unit/ --maxfail=1 --exitfirst -v
```

Or use VS Code: **[TEST][UNIT] Backend unit tests**

## Configuration

- **Fail-fast**: Enabled (`--maxfail=1 --exitfirst`)
- **Timeout**: 5 seconds per test (default)
- **Deterministic**: All tests exit cleanly

## Writing Unit Tests

Keep unit tests:
- **Fast** - Should complete in milliseconds
- **Isolated** - No external dependencies
- **Focused** - Test one thing at a time
- **Deterministic** - Same input = same output

## Example

See `test_example.py` for a basic unit test template.

# Tests

This directory contains all tests for the Barkibu Claims Automation system.

## Structure

- `unit/` - Unit tests for individual components and functions
- `regression/` - End-to-end regression tests simulating real client behavior

## Testing Philosophy

### Fail-Fast Approach
All tests are configured to exit immediately on:
- Uncaught exceptions
- Runtime errors
- Failed assertions
- Test crashes

No retries, no "continue on error", no hanging processes.

### Test Requirements
Every feature MUST include:
1. **Unit tests** - Test individual components in isolation
2. **Regression tests** - Simulate real frontend → backend interactions

## Running Tests

### All Tests

```bash
pytest tests/ --maxfail=1 --exitfirst -v
```

Or use VS Code: **[TEST][UNIT] Backend unit tests** or **[TEST][REGRESSION] Full regression suite**

### Unit Tests Only

```bash
pytest tests/unit/ --maxfail=1 --exitfirst -v
```

### Regression Tests Only

```bash
pytest tests/regression/ --maxfail=1 --exitfirst -v
```

## Configuration

### pytest Configuration
- `--maxfail=1` - Stop after first failure
- `--exitfirst` - Exit immediately on first error
- `-v` - Verbose output
- All tests have explicit timeouts
- Deterministic termination guaranteed

### Test Timeouts
All tests must complete within reasonable timeouts:
- Unit tests: 5 seconds default
- Regression tests: 30 seconds default

## Writing Tests

### Unit Test Example

```python
import pytest
from app.some_module import some_function

def test_some_function():
    """Test that some_function works correctly."""
    result = some_function(input_data)
    assert result == expected_output
```

### Regression Test Example

```python
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_full_workflow():
    """Test complete user workflow from upload to extraction."""
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Simulate frontend → backend interaction
        response = await client.post("/upload", files={"file": test_file})
        assert response.status_code == 200
```

## Best Practices

1. **Descriptive names** - Test names should clearly describe what is being tested
2. **One assertion per test** - Keep tests focused and simple
3. **Arrange-Act-Assert** - Structure tests clearly
4. **No test interdependencies** - Each test should be independent
5. **Clean up resources** - Use fixtures for setup and teardown
6. **Fail fast** - Don't try to recover from errors in tests

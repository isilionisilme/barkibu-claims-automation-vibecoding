# tmp/

This directory is for **temporary and throwaway scripts only**.

## Purpose

Use this directory for:
- One-off scripts
- Quick experiments
- Temporary data processing
- Debugging utilities
- Throwaway code

## Important Rules

1. **No reusable code** - If code is reusable, it belongs elsewhere
2. **Not committed** - Files here should generally not be committed to git
3. **No production dependencies** - Production code should never depend on tmp/
4. **Clean up regularly** - Delete files when no longer needed

## Where to Put Reusable Code

If you're writing code that should be reused:

- **Backend code** → `backend/app/`
- **Frontend code** → `frontend/src/`
- **Tests** → `tests/`
- **Benchmarks** → `benchmark/`
- **Scripts** → Create a `scripts/` directory with proper documentation

## Examples of tmp/ Usage

✅ **Good uses**:
- `tmp/test_data_generator.py` - One-off script to generate test data
- `tmp/debug_issue_123.py` - Temporary debugging script
- `tmp/experiment_new_library.py` - Testing a new library before integration

❌ **Bad uses**:
- `tmp/utils.py` - Reusable utilities (should be in backend/app/utils.py)
- `tmp/api_client.py` - Reusable API client (should be properly organized)
- `tmp/important_feature.py` - Production feature (belongs in main codebase)

## Cleanup

Periodically review and delete files in tmp/ that are no longer needed.

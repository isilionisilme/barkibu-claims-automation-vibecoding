# Benchmarks

This directory contains performance benchmarks for the Barkibu Claims Automation system.

## Purpose

Benchmarks measure and track:
- API endpoint latency
- Document processing throughput
- Memory usage
- Database query performance
- Overall system performance

## Running Benchmarks

```bash
python benchmark/bench_api.py
```

Or use VS Code: **[BENCH][API] API benchmarks**

## Output

Benchmarks output measurable metrics:
- **Latency** - Response time in milliseconds
- **Throughput** - Requests per second
- **Memory** - Memory usage in MB
- **Success Rate** - Percentage of successful operations

Results are printed to console in a structured format.

## Writing Benchmarks

Benchmarks should:
- **Measure real operations** - Use actual code paths
- **Report metrics** - Output quantifiable results
- **Be repeatable** - Same conditions = same results
- **Document baseline** - Track performance over time

## Interpreting Results

Compare benchmark results over time to:
- Detect performance regressions
- Validate optimizations
- Identify bottlenecks
- Set performance budgets

## Example

See `bench_api.py` for a basic benchmark template.

## Best Practices

1. **Run multiple iterations** - Average results for accuracy
2. **Warm up** - Run once before measuring to warm caches
3. **Isolate variables** - Control external factors
4. **Document environment** - Note hardware, OS, Python version
5. **Track over time** - Keep historical results for comparison

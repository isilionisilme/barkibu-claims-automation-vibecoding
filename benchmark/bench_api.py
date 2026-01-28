"""
API Performance Benchmarks

This script benchmarks API endpoint performance, measuring:
- Latency (response time)
- Throughput (requests per second)
- Success rate

Output includes measurable metrics for tracking performance over time.
"""

import asyncio
import time
import statistics
from typing import List, Dict
import sys
from pathlib import Path

# Add backend to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "backend"))

from httpx import AsyncClient
from backend.app.main import app


class BenchmarkResults:
    """Container for benchmark results."""
    
    def __init__(self, name: str):
        self.name = name
        self.latencies: List[float] = []
        self.successes = 0
        self.failures = 0
    
    def add_result(self, latency: float, success: bool):
        """Add a benchmark result."""
        self.latencies.append(latency)
        if success:
            self.successes += 1
        else:
            self.failures += 1
    
    def print_results(self):
        """Print formatted benchmark results."""
        total = self.successes + self.failures
        success_rate = (self.successes / total * 100) if total > 0 else 0
        
        print(f"\n{'=' * 60}")
        print(f"Benchmark: {self.name}")
        print(f"{'=' * 60}")
        print(f"Total Requests:    {total}")
        print(f"Successful:        {self.successes}")
        print(f"Failed:            {self.failures}")
        print(f"Success Rate:      {success_rate:.2f}%")
        
        if self.latencies:
            print(f"\nLatency Metrics (ms):")
            print(f"  Min:             {min(self.latencies) * 1000:.2f}")
            print(f"  Max:             {max(self.latencies) * 1000:.2f}")
            print(f"  Mean:            {statistics.mean(self.latencies) * 1000:.2f}")
            print(f"  Median:          {statistics.median(self.latencies) * 1000:.2f}")
            if len(self.latencies) > 1:
                print(f"  Std Dev:         {statistics.stdev(self.latencies) * 1000:.2f}")
            
            # Calculate throughput
            total_time = sum(self.latencies)
            throughput = total / total_time if total_time > 0 else 0
            print(f"\nThroughput:        {throughput:.2f} requests/second")
        
        print(f"{'=' * 60}\n")


async def benchmark_endpoint(
    client: AsyncClient,
    method: str,
    path: str,
    iterations: int = 100,
    warmup: int = 10
) -> BenchmarkResults:
    """
    Benchmark a single endpoint.
    
    Args:
        client: HTTP client
        method: HTTP method (GET, POST, etc.)
        path: Endpoint path
        iterations: Number of iterations to run
        warmup: Number of warmup iterations (not measured)
    
    Returns:
        BenchmarkResults object with metrics
    """
    results = BenchmarkResults(f"{method} {path}")
    
    # Warmup phase
    print(f"Warming up {method} {path} ({warmup} iterations)...")
    for _ in range(warmup):
        await client.request(method, path)
    
    # Benchmark phase
    print(f"Benchmarking {method} {path} ({iterations} iterations)...")
    for i in range(iterations):
        start_time = time.perf_counter()
        try:
            response = await client.request(method, path)
            success = response.status_code == 200
        except Exception:
            success = False
        end_time = time.perf_counter()
        
        latency = end_time - start_time
        results.add_result(latency, success)
        
        # Progress indicator
        if (i + 1) % 20 == 0:
            print(f"  Progress: {i + 1}/{iterations}")
    
    return results


async def run_benchmarks():
    """Run all API benchmarks."""
    print("\n" + "=" * 60)
    print("API Performance Benchmarks")
    print("=" * 60)
    print(f"Starting at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    async with AsyncClient(app=app, base_url="http://test") as client:
        # Benchmark root endpoint
        root_results = await benchmark_endpoint(
            client, "GET", "/", iterations=100, warmup=10
        )
        root_results.print_results()
        
        # Benchmark health check endpoint
        health_results = await benchmark_endpoint(
            client, "GET", "/health", iterations=100, warmup=10
        )
        health_results.print_results()
    
    print(f"Completed at: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    print("Barkibu Claims Automation - API Benchmarks")
    print("This will measure API endpoint performance.\n")
    
    # Run benchmarks
    asyncio.run(run_benchmarks())
    
    print("Benchmark complete!")
    print("\nTip: Run benchmarks regularly to track performance over time.")
    print("Consider saving results to a file for historical comparison.")

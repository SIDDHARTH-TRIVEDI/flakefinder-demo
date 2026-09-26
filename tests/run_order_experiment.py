import os
import random
import subprocess
import sys


TEST_TARGET = "tests/test_a_order.py"
TEST_MUTATOR = "tests/test_shared_cache_mutator.py"

TOTAL_RUNS = 20

passes = 0
failures = 0

seed_env = os.getenv("FLAKE_DEMO_SEED")
rng = random.Random(int(seed_env)) if seed_env is not None else random

print("FlakeFinder - Test Order Experiment")
print("=" * 45)
if seed_env is not None:
    print(f"FLAKE_DEMO_SEED: {seed_env}")

for run in range(1, TOTAL_RUNS + 1):

    # Randomly choose which test runs first
    if rng.choice([True, False]):
        order = [TEST_TARGET, TEST_MUTATOR]
    else:
        order = [TEST_MUTATOR, TEST_TARGET]

    print(f"\nRun {run}/{TOTAL_RUNS}")
    print(f"Order: {' -> '.join(order)}")

    result = subprocess.run(
        [sys.executable, "-m", "pytest", *order, "-q"],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        passes += 1
        print("Result: PASS")
    else:
        failures += 1
        print("Result: FAIL")

print("\n" + "=" * 45)
print("EXPERIMENT RESULTS")
print("=" * 45)

print(f"Total runs : {TOTAL_RUNS}")
print(f"Passes     : {passes}")
print(f"Failures   : {failures}")

pass_rate = (passes / TOTAL_RUNS) * 100

print(f"Pass rate  : {pass_rate:.1f}%")
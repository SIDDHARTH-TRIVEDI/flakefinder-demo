import os
import subprocess
import sys

TOTAL_RUNS = 20
passes = 0
failures = 0

seed_env = os.getenv("FLAKE_DEMO_SEED")

print("FlakeFinder - Test D Regression Experiment")
print("=" * 45)
if seed_env is not None:
    print(f"FLAKE_DEMO_SEED: {seed_env}")

for run in range(1, TOTAL_RUNS + 1):
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/test_d_regression.py", "-q"],
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        passes += 1
        print(f"Run {run}/20: PASS")
    else:
        failures += 1
        print(f"Run {run}/20: FAIL")

print("\n" + "=" * 45)
print("EXPERIMENT RESULTS")
print("=" * 45)

print(f"Total runs : {TOTAL_RUNS}")
print(f"Passes     : {passes}")
print(f"Failures   : {failures}")
print(f"Pass rate  : {(passes / TOTAL_RUNS) * 100:.1f}%")

import random
import subprocess
import sys


TEST_A = "tests/test_a_order.py"
TEST_B = "tests/test_b_race.py"

TOTAL_RUNS = 20

passes = 0
failures = 0


print("FlakeFinder - Test Order Experiment")
print("=" * 45)

for run in range(1, TOTAL_RUNS + 1):

    # Randomly choose which test runs first
    if random.choice([True, False]):
        order = [TEST_A, TEST_B]
    else:
        order = [TEST_B, TEST_A]

    print(f"\nRun {run}/20")
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
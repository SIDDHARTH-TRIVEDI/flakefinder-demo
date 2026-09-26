# FlakeFinder Demo Verification

Empirical results from Step 1 verification of the FlakeFinder demo test cases.

## Test A — Order Dependency
* **Test Run Alone**:
  * Command: `pytest tests/test_a_order.py`
  * Result: **PASS** (1/1 passed)
* **Correct Order** (`test_a_order.py` before `test_shared_cache_mutator.py`):
  * Command: `pytest tests/test_a_order.py tests/test_shared_cache_mutator.py`
  * Result: **PASS** (2/2 passed)
* **Reversed Order** (`test_shared_cache_mutator.py` before `test_a_order.py`):
  * Command: `pytest tests/test_shared_cache_mutator.py tests/test_a_order.py`
  * Result: **FAIL** (1 failed, 1 passed; `test_cache_starts_clean` fails: `assert 'contaminated' == 'clean'`)

## Test B — Async Race Condition
* **10-Run Verification** (`FLAKE_DEMO_SEED` unset):
  * Total runs: 10
  * Passes: 9
  * Failures: 1
  * Pass rate: **90.0%**
  * Failure rate: **10.0%**

## Test C — Nondeterministic Randomness
* **10-Run Verification** (`FLAKE_DEMO_SEED` unset):
  * Total runs: 10
  * Passes: 7
  * Failures: 3
  * Pass rate: **70.0%**
  * Failure rate: **30.0%**

## Test D — Current Good State
* **Good State Verification** (Commit `c05ee70` through `22aa6eb` where `calculate_total` returns `sum(items)`):
  * Command: `pytest tests/test_d_regression.py`
  * Expected: `calculate_total([10, 20, 30]) == 60`
  * Result: **PASS** (100% reliable pass rate before regression)

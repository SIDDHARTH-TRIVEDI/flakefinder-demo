# FlakeFinder Test A Baseline

## Test
Shared-state / test-order dependency (`tests/test_a_order.py` paired with `tests/test_shared_cache_mutator.py`).

## Baseline experiment
20 randomized execution-order trials with `FLAKE_DEMO_SEED` unset.

- Total runs: 20
- Passes: 11
- Failures: 9
- Pass rate: 55.0%
- Failure rate: 45.0%

## Observed behavior

`test_a_order.py -> test_shared_cache_mutator.py`:
- Result: PASS (11/11 trials)

`test_shared_cache_mutator.py -> test_a_order.py`:
- Result: FAIL (9/9 trials)

## Preliminary hypothesis
`test_shared_cache_mutator.py` mutates module-level shared state (`src/shared_cache.py`'s `shared_cache["user"] = "contaminated"`) and does not reset it. When `test_a_order.py` runs after the mutator test, its precondition assertion `assert shared_cache["user"] == "clean"` fails.

When `test_a_order.py` runs in isolation or before the mutator test, it passes reliably.

## Historical Note
An earlier version of the experiment incorrectly paired Test A with `tests/test_b_race.py`. The experiment now correctly isolates the shared-state dependency with a dedicated cache mutator test (`test_shared_cache_mutator.py`).

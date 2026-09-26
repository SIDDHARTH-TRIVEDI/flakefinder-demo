# FlakeFinder Test D Baseline

## Test
Git regression flakiness (`tests/test_d_regression.py` testing `src/regression.py`).

## Baseline experiment
20 runs with `FLAKE_DEMO_SEED` unset.

- Total runs: 20
- Passes: 13
- Failures: 7
- Pass rate: 65.0%
- Failure rate: 35.0%

## Observed behavior
The test intermittently fails:
`assert 61 == 60` where `61 = calculate_total([10, 20, 30])`.

An off-by-one error was introduced into `calculate_total` that intermittently adds 1 to the calculated total.

## Preliminary hypothesis
Commit `04805c1` ("Introduce regression causing flaky calculation") introduced an unseeded random branch in `calculate_total`:
```python
if random.random() < 0.5:
    total += 1
```
Prior to commit `04805c1` (from commit `c05ee70` through commit `22aa6eb`), `calculate_total` deterministically returned `sum(items)`. A `git bisect` between good commit `c05ee70` and bad commit `04805c1` cleanly isolates `04805c1` as the regression culprit.

## Important
This is baseline evidence before any fix.

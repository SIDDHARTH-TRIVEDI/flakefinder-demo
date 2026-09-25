\# FlakeFinder Test A Baseline



\## Test

Shared-state / test-order dependency



\## Baseline experiment



20 randomized execution-order trials.



\- Total runs: 20

\- Passes: 8

\- Failures: 12

\- Pass rate: 40.0%

\- Failure rate: 60.0%



\## Observed behavior



A -> B:

PASS



B -> A:

FAIL



\## Preliminary hypothesis



Test B modifies module-level shared state and does not

reset it before Test A executes.



This causes Test A to fail when Test B runs before it.



\## Important



This is baseline evidence before any fix.

Do not modify these results.


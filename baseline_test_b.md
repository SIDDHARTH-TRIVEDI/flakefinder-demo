\# FlakeFinder Test B Baseline



\## Test

Async race condition



\## Baseline experiment



20 runs with FLAKE\_DEMO\_SEED unset.



\- Total runs: 20

\- Passes: 17

\- Failures: 3

\- Pass rate: 85.0%

\- Failure rate: 15.0%



\## Observed behavior



The test intermittently fails because the background

task is started but not awaited.



\## Preliminary hypothesis



A missing await creates a race between the background

update and the assertion.



\## Important



This is baseline evidence before any fix.


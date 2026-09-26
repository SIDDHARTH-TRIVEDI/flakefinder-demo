\# FlakeFinder Test C Baseline



\## Test

Nondeterministic randomness



\## Baseline experiment



20 runs with FLAKE\_DEMO\_SEED unset.



\- Total runs: 20

\- Passes: 9

\- Failures: 11

\- Pass rate: 45.0%

\- Failure rate: 55.0%



\## Observed behavior



The same test produces different results because the

application uses an unseeded random value.



\## Preliminary hypothesis



Uncontrolled randomness makes the test result nondeterministic.



\## Important



This is baseline evidence before any fix.


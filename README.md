# EHR Upgrade UAT Framework

This is a small UAT tracker I built for a pretend EHR upgrade. I wanted to work through the questions a test lead has to answer before go-live: what did we test, what broke, which defects are still open, and are we actually ready?

All of the data is made up. There are no real patients, facilities, or PHI in this repo.

## How it works

Every test case is one row in `data/test_cases.csv`:

```
case_id,module,scenario,expected_result,status,defect_id
U003,Scheduling,Reschedule appointment,Updated slot visible,fail,D001
```

`src/main.py` reads the file and works out:

- the overall pass rate
- pass/fail/blocked counts for each module (Registration, Scheduling, Clinical, Billing, Reporting)
- which defect IDs are still open, meaning they're tied to a failed or blocked case
- a release gate: `READY FOR REVIEW` or `REVIEW REQUIRED`

It prints the result and also saves it to `output/uat_summary.json`.

## Running it

You only need Python 3.10 or newer. There's nothing to install.

```bash
python src/main.py
python -m unittest discover -s tests
```

Run both commands from the repo root.

## Current results

With the sample data I have now:

| Module       | Pass | Fail | Blocked |
|--------------|------|------|---------|
| Registration | 1    |      |         |
| Scheduling   | 1    | 1    |         |
| Clinical     | 2    |      |         |
| Billing      | 1    |      |         |
| Reporting    |      |      | 1       |

That's 7 cases, a 71.4% pass rate, and 2 open defects:

- **D001**: rescheduling doesn't show the updated slot
- **D002**: the encounter export is blocked, so the counts can't be verified

The gate comes out as **REVIEW REQUIRED**.

## Some decisions I made

- **Blocked counts separately from failed.** A blocked test means we couldn't check it at all, which is a different problem from "we checked and it's wrong." Lumping the two together hides the real state of testing.
- **`not_run` also blocks the gate.** If a test was never executed, I don't want the summary saying everything is fine. Any fail, blocked, or not-run case flips the gate to `REVIEW REQUIRED`.
- **The script rejects bad status values.** If someone types `passed` or `Fail` in the CSV, it raises an error. Without that check, the row would just disappear from the counts.
- **The best result is "ready for review", not "ready to deploy".** The script can't approve a go-live. Sign-off from the business owner, the rollback plan, and so on still happen outside it. The checklist for those is in `docs/uat-plan.md`.
- **CSV instead of a database.** Testers already live in spreadsheets, and a CSV is easy to diff in git.

## Files

```
data/test_cases.csv     test cases and their results
docs/uat-plan.md        scope, evidence template, release gate checklist
src/main.py             builds the summary
tests/test_main.py      unit tests for the gate and pass-rate logic
output/                 generated summary (created when you run the script)
```

## What I'd add next

- A severity column, so the gate only blocks on critical or high defects
- Tester name and execution date on each run, to match the evidence template
- A simple HTML report alongside the JSON
- More tests covering empty files and bad status values

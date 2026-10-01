# Release plan

Written before the release, so readers can check the release against it. The work on this release runs from October to December 2026. Changes to this plan are recorded at the bottom with a date and a reason.

## What is measured

- Ten families of document-poisoning attacks against a local question-answering assistant that answers from a document set pinned to one git commit.
- Four existing open-weight models, unmodified, each version recorded by digest.
- Four defenses (system instruction, sanitizer, link filter, provenance check), each alone and all combined.
- Two poison states: unapproved (never in an approved commit) and approved (arrived through an approved change).
- Usefulness with defenses on: factual questions answered correctly, and "not in the documents" when the answer is absent.
- One established external scanner (garak) and, in the final runs, PyRIT and the BIPIA and LLMail-Inject datasets.

## How it is scored

- Deterministic local scoring per attack family; no judge model in the scoring itself.
- Every automatic "success" and a random sample of automatic "blocked" results are reviewed by an LLM reviewer with a fixed rubric; a second LLM reviewer re-checks the disagreements. This is not a human review; the report adds the author's own check of a random sample and reports the agreement.
- Results are reported as k/n per cell with Wilson 95% intervals. Small n means wide intervals; "0 of 60" is not "zero risk".

## What will be published

- Harness, scoring, configs, hash-locked dependency files and the environment record.
- Aggregate tables per model, defense and poison state, with intervals, and how often the automatic scoring was wrong.
- A short technical report: threat model, method, results, what did not work, limits.
- A one-command rerun, a check that model digests, runtime version and corpus commit match before each run, and a 10% repeat run that reports how many outcomes are identical.
- If an external rerun takes place: its results next to the original ones, including every difference.

## What will not be published

Attack texts (on request for researchers, after fixes), canary strings, keys and raw model answers. See `DISCLOSURE-POLICY.md`.

## Changes to this plan

- (none yet)

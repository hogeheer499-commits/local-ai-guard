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

- The own attack harness uses deterministic local scoring per attack family. The adapted BIPIA subset was partly scored by a local judge model; that benchmark scoring is reported separately.
- Every automatic "success" and a random sample of automatic "blocked" results are reviewed by an LLM reviewer with a fixed rubric; a second LLM reviewer re-checks the disagreements. This is not independent human review. The proposed follow-up includes a fixed stratified 100-answer sample scored by the author and an outside reviewer, with condition and earlier labels hidden from the outside reviewer; agreement will be reported per group.
- Results are reported as k/n per cell with Wilson 95% intervals. Small n means wide intervals; "0 of 60" is not "zero risk".

## What will be published

- Harness, scoring, configs, hash-locked dependency files and the environment record.
- Aggregate tables per model, defense and poison state, with intervals, and how often the automatic scoring was wrong.
- A short technical report: threat model, method, results, what did not work, limits.
- A one-command rerun, a check that model digests, runtime version and corpus commit match before each run, and a repeat check on one selected attack type that reports automatic outcome agreement and its limited coverage.
- If an external rerun takes place: its results next to the original ones, including every difference.

## What will not be published

Attack texts (on request for researchers, after fixes), canary strings, keys and raw model answers. See `DISCLOSURE-POLICY.md`.

## Changes to this plan

- 4 October 2026: preliminary aggregate results, method, table script and publication hashes published ahead of the full release. Measured defense code remains private until that release, with inspection copies available to grant reviewers on request. Corrected the scoring description to distinguish the own harness from BIPIA judge-model scoring, and the repeat description to identify its selected attack type rather than imply a random sample across attacks. These updates describe the recorded work and planned validation; they do not alter historical results.

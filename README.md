# local-ai-guard

A small local question-answering assistant that answers only from an approved set of documents, plus an evaluation of how well its defenses hold up against poisoned documents.

**Status (October 2026):** the main runs of the evaluation (version 0.2.0, "v5") are complete; the last external-tool runs and the final checks are in progress. The harness, aggregate results and a short technical report will be published in this repository; the release is planned for this autumn. Until then this repository holds the threat model, the policies and the method description. No results are published yet.

## What it is

- A Python package (no third-party dependencies) that serves answers from a document set pinned to one approved git commit, with a provenance check, a sanitizer, a link filter and a system instruction as separable defenses.
- An evaluation harness that runs ten families of document-poisoning attacks against four existing open-weight models (unmodified, each version recorded by digest), with every defense measured alone and combined, and with the poison both unapproved and approved.
- Established external tools run against the same setup (garak; PyRIT and the BIPIA and LLMail-Inject datasets in the final runs).

## Threat model, in short

An assistant that answers from documents treats retrieved text as trustworthy. Anyone who can place or alter a document in that set can try to steer answers: hidden instructions, forged figures, or a link that leaks the user's question. Two cases are measured:

1. **Unapproved poison:** the poisoned document never entered an approved commit. This is the case most defenses are tested on.
2. **Approved poison:** the poisoned document arrived through an approved change (a careless or malicious commit). This is the harder, realistic case: which checks still help once a human has signed off?

The first round of this evaluation (v4) was adversarially reviewed; the review showed that the provenance defense only looked perfect because the poison was never in an approved commit. The second round exists to measure the approved case properly.

## What will be published, and what will not

See `DISCLOSURE-POLICY.md`. In short: attack categories, counts, hashes, the harness and the scoring are public; attack texts are available to researchers on request after fixes; canary strings, keys and raw model answers are never published.

## Reproducibility

The release includes one command to rerun the evaluation, hash-locked dependency files for the external tools, an environment record (model digests, runtime versions, corpus commit) and a repeat run that reports how many outcomes are identical. An external rerun by a person outside this setup is planned; its results will be published next to the original ones.

## Licenses

Code: MIT. Tables, dataset card and report: CC BY 4.0. See `LICENSES.md` and `THIRD-PARTY.md`.

## Use of AI assistance

Parts of the harness were written with AI assistance. `AI-USAGE.md` records which parts, who reviewed them and how they were tested.

## Security

Please report vulnerabilities privately; see `SECURITY.md`.

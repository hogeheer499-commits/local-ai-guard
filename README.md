# local-ai-guard

A small local question-answering assistant that answers only from an approved set of documents, plus an evaluation of how well its defenses hold up against poisoned documents.

**Status (October 2026):** [Preliminary aggregate results, method and limits](EVIDENCE-SUMMARY.md) are now public, with [machine-readable tables](RESULTS-PRELIMINARY.csv), a [table-generation script](make-evidence-table.py) and [publication hashes](EVIDENCE-SHA256.txt). The results concern evaluation v5, using the original measured defense code (package version 0.1.0). Counts were checked with LLM assistance, not yet independently scored by humans or replicated outside this setup. Defense modules are available privately to grant reviewers on request; the documented code, full harness and technical report follow in the research release.

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

See `DISCLOSURE-POLICY.md`. In short: preliminary aggregate counts and method are public now; attack categories, item hashes, the harness and scoring are planned for the research release; attack texts are available to researchers on request after fixes; canary strings, keys and raw model answers are never published.

## Reproducibility

The planned release includes one command to rerun the evaluation, hash-locked dependency files for the external tools, an environment record (model digests, runtime versions, corpus commit) and a repeat check with its selected attack type and outcome agreement reported explicitly; it is not a representative random sample across attack types. An external rerun by a person outside this setup is planned; its results will be published next to the original ones.

## Licenses

Code: MIT. Tables, dataset card and report: CC BY 4.0. See `LICENSES.md` and `THIRD-PARTY.md`.

## Use of AI assistance

Parts of the harness were written with AI assistance. `AI-USAGE.md` records which parts, who reviewed them and how they were tested.

## Security

Please report vulnerabilities privately; see `SECURITY.md`.

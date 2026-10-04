# local-ai-guard: preliminary evidence

Results from evaluation v5, documented 3 October and published 4 October 2026. Code and the complete research release are not published in this evidence package. The counts were checked by LLM reviewers; independent human scoring and replication are still outstanding.

## Main finding

The combined defenses stopped the fixed instruction-related attacks in these tests, but did not stop forged figures. The sanitizer could make a forged CSV row easier to retrieve: the row was retrieved in 24/24 tested cases with sanitization and 0/24 without it. Retrieval of a row is distinct from accepting its figure in an answer.

## Setting

Four existing open-weight models, all 4-bit, on Ollama 0.32.15. The document corpus was the author's public Strix Halo guide, revision `b34b6ac887729cbd51e2a2ffe538d8810a2a896f`. The poisoned revision was approved by the author as an experimental condition; this was not a study of real human reviewers.

Ten attack types, six repeats per type and model, 60 attempts per model and defense condition. The repeats are correlated. The defenses were measured separately and together: a system prompt, sanitizer, link filter and provenance check. The provenance check cannot reject a poisoned document already inside the approved revision.

## Counts with approved poison

| Defense | Instruction-related attacks | Forged figures | Total |
|---|---:|---:|---:|
| No defense | 56/192 | 13/48 | 69/240 |
| System prompt | 10/192 | 13/48 | 23/240 |
| Sanitizer | 4/192 | 28/48 | 32/240 |
| Link filter | 41/192 | 13/48 | 54/240 |
| Provenance check | 62/192 | 14/48 | 76/240 |
| All four | 0/192 | 24/48 | 24/240 |

The combined total of 24/240 and the system-prompt total of 23/240 conceal different effects; they do not establish equivalence or superiority. A10 overlaps with genuine text in the corpus. Excluding that type gives 39/168 instruction-related successes without defenses and 0/168 with all four; the forged-figure counts remain 13/48 and 24/48.

## Counts per model

Each cell is successes out of 60 attempts, with approved poison. The CSV also reports counts with A10 excluded (54 attempts per model).

| Model | None | Prompt | Sanitizer | Links | Provenance | All four |
|---|---:|---:|---:|---:|---:|---:|
| devstral-small-2:latest | 15 | 2 | 9 | 12 | 14 | 9 |
| qwen2.5vl:7b | 15 | 8 | 9 | 15 | 17 | 5 |
| qwen3.6:35b-a3b | 22 | 7 | 3 | 12 | 25 | 3 |
| qwen3.8:27b-q4_K_M | 17 | 6 | 11 | 15 | 20 | 7 |

## Limits and checks

- Preliminary after LLM review, without independent human labels or an outside rerun.
- One document collection and one runtime; fixed attacks rather than a comprehensive adaptive evaluation. No general safety claim follows from a zero count.
- Counts concern the measured version. A later link-filter patch is not validated by these original results and requires a separately labelled check.
- A repeat comparison on one selected attack type matched 293/312 automatic outcomes (93.9%). This is not a random 10% sample across all attack types, nor proof of bit-identical reproduction.
- Unapproved documents are rejected by the provenance check by design; zero successes in that condition are not evidence that the underlying model is immune.
- The supplied table script recomputes tables from the CSV. It does not rerun model tests, independently validate labels or reproduce the original experiment.

## Remaining work proposed for funding

A transferable research release and clean-install check; versioned checking of the later link-filter patch; an outside rerun for one model; independent hand-scoring of 100 original answers with condition and earlier labels hidden, subject to confirming the scorer; and a report comparing the checks with these original counts. Original runs and work already completed are not charged again. The outside scorer and funding are not yet confirmed.

The measured defense modules can be supplied privately to grant reviewers on request. This permits implementation inspection, not a complete experimental rerun. The planned research release will include the code and configuration needed to check these research results. Attack fixtures follow the repository's disclosure policy. Customer-specific integrations and services are separate work; none are claimed as already delivered here.

## Model digests

- `devstral-small-2:latest`: `24277f07f62db8f9cb68e9dfc679ea1818a7fbac47a50eff0a701d3f645b63c8`
- `qwen2.5vl:7b`: `5ced39dfa4bac325dc183dd1e4febaa1c46b3ea28bce48896c8e69c1e79611cc`
- `qwen3.6:35b-a3b`: `096fdbd02fe620fc10cbeb6537e080f8041aece851e5d696aed024d4f70f2e47`
- `qwen3.8:27b-q4_K_M`: `25b843619e944cd0ae6069f94ff4e5e26a16e109ccbc0a66a0f05979ed70098e`

## Files and license

`RESULTS-PRELIMINARY.csv` contains 24 model-condition rows and 12 pooled attack-group rows. `make-evidence-table.py` checks their arithmetic and prints the two tables. `EVIDENCE-SHA256.txt` records the bytes in this evidence package; these are post-run publication fingerprints, not preregistration.

Tables and this note: CC BY 4.0. Table-generation script: MIT. Published 4 October 2026. These hashes are post-run publication fingerprints, not preregistration.

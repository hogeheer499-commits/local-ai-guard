# local-ai-guard: preliminary evidence

Results from evaluation v5, documented 3 October and published 4 October 2026. Code and the complete research release are not published in this evidence package. The counts were checked by LLM reviewers; independent human scoring and replication are still outstanding.

## Main finding

Prompt injection through documents worked against all four local models without safeguards: 56/192 instruction-related attacks succeeded with approved poison. With all four safeguards combined, 0/192 succeeded in these tests. Testing each safeguard separately also exposed a side effect: the sanitizer removed a suspicious note from a forged CSV row but kept the false number, and that row became easier to retrieve (24/24 tested cases with sanitization, 0/24 without). Forged-figure attacks rose from 13/48 to 24/48 with all four safeguards; in the CSV case, 13/24 answers were provisionally labelled as presenting the forged figure as correct. Retrieving the row is a separate outcome from accepting the forgery. This trace concerns one CSV case and does not explain every forged-figure result.

## Setting

Four existing open-weight models, all 4-bit, on Ollama 0.32.15. The document corpus was the author's public Strix Halo guide, revision `b34b6ac887729cbd51e2a2ffe538d8810a2a896f`. The poisoned revision was approved by the author as an experimental condition; this was not a study of real human reviewers.

Ten attack types, six repeats per type and model, 60 attempts per model and defense condition. The repeats are correlated. The defenses were measured separately and together: a system prompt, sanitizer, link filter and provenance check. The provenance check cannot reject a poisoned document already inside the approved revision.

The grouping into instruction-related attacks (A1, A2, A5-A10) and forged figures (A3, A4) was made after seeing the results. It is a post-hoc analysis, not a preregistered comparison. Counts by individual type remain part of the planned full research release.

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

## Supporting results

These are separate checks from the original own attack suite. They use the same four principal models. Counts come from the recorded v5 aggregates; independent human validation remains pending.

### Usefulness

Factual answers labelled correct, out of 40 per model in the committed-corpus setup:

| Model | No defense | All four |
|---|---:|---:|
| devstral-small-2:latest | 39/40 | 40/40 |
| qwen2.5vl:7b | 38/40 | 35/40 |
| qwen3.6:35b-a3b | 37/40 | 40/40 |
| qwen3.8:27b-q4_K_M | 40/40 | 40/40 |
| Total | 154/160 | 155/160 |

The pooled counts conceal a decline for the 7B model. They do not establish an improvement in usefulness. With all defenses, each model also declined all five questions the guide could not answer (20/20 across models). Those are five question designs tested on four models, not 20 distinct questions. These are recorded automated scoring outcomes, not independent human validation or evidence of general usefulness beyond this question set.

### Adapted BIPIA subset

This adaptation used 75 items: 25 with local deterministic scoring and 50 with a local judge model (`qwen3.8:27b-q4_K_M`), followed by LLM-assisted checking. Independent human validation remains pending. The table reports successful attacks / valid retrieved-answer cases in the committed-poison run, with source approval where provenance applies.

| Defense | Devstral Small 2 | Qwen2.5-VL 7B | Qwen3.6 35B-A3B | Qwen3.8 27B | Total |
|---|---:|---:|---:|---:|---:|
| No defense | 3/74 | 0/74 | 9/74 | 9/74 | 21/296 |
| System prompt | 0/74 | 0/74 | 0/74 | 0/74 | 0/296 |
| Sanitizer | 4/73 | 1/74 | 7/74 | 6/74 | 18/295 |
| Link filter | 3/74 | 0/74 | 9/74 | 8/74 | 20/296 |
| Provenance check | 3/74 | 0/74 | 9/74 | 7/74 | 19/296 |
| All four | 0/74 | 0/74 | 0/74 | 0/74 | 0/296 |

There were 300 scheduled cases per setting (75 items on four models), without the six-repeat design of the own attack suite. Four cases per setting were excluded because the attack material was not retrieved. The sanitizer setting had one additional execution error, leaving 295 valid cases; the other displayed settings had 296. Excluded cases are not counted as successful defense outcomes. This is an adaptation, not a reproduction of the paper's reported benchmark results or evidence of general immunity. [BIPIA paper](https://arxiv.org/abs/2312.14197).

### Repeat check: A2 only

The same author reran one of the ten fixed attack types, A2, selected by the repeat script's seed. This compared 312 of the original 3,120 attack measurements across committed and memory poison modes. The original automatic labels matched in 293/312 cases (93.9%, rounded to 94%); 19 differed. It was not an outside replication or a random sample of measurements across attack types.

| Model | Automatic labels matched, all settings | Automatic labels matched, all-four settings |
|---|---:|---:|
| devstral-small-2:latest | 77/78 | 12/12 |
| qwen2.5vl:7b | 78/78 | 12/12 |
| qwen3.6:35b-a3b | 70/78 | 12/12 |
| qwen3.8:27b-q4_K_M | 68/78 | 12/12 |
| Total | 293/312 | 48/48 |

The all-four column includes both approved and unapproved source conditions (six measurements per model per condition). Agreement concerns automatic outcome labels, not identical answer text. It does not repeat the forged-figure attack types A3/A4 or independently validate any label. Later LLM-corrected labels are separate from this automatic comparison.

Automatic-label agreement by defense and document status:

| Defense and document status | Matched | Compared | Changed |
|---|---:|---:|---:|
| No defense | 40 | 48 | 8 |
| System prompt | 48 | 48 | 0 |
| Sanitizer | 48 | 48 | 0 |
| Link filter | 39 | 48 | 9 |
| Provenance check, approved | 22 | 24 | 2 |
| Provenance check, unapproved | 48 | 48 | 0 |
| All four, approved | 24 | 24 | 0 |
| All four, unapproved | 24 | 24 | 0 |
| Total | 293 | 312 | 19 |

Rows pool the four models and both poison modes where that setting was run. Approved all-four cases belong to the committed-poison run; unapproved all-four cases to the memory-poison run. All 48 all-four labels were blocked in both runs. Committed-poison labels matched in 158/168 cases; memory-poison labels in 135/144. No comparison key was duplicated or missing its baseline counterpart. Fourteen labels changed from blocked to successful; five changed from successful to blocked. The repeat kept the original seeds and temperatures: 52 measurements at temperature 0 and 260 at temperature 0.7. The two modes are repeated settings, not independent attack designs.

## Limits and checks

- Preliminary after LLM review, without independent human labels or an outside rerun.
- One document collection and one runtime; fixed attacks rather than a comprehensive adaptive evaluation. No general safety claim follows from a zero count.
- Counts concern the measured version. A later link-filter patch is not validated by these original results and requires a separately labelled check.
- The A2-only repeat matched 293/312 automatic outcomes (93.9%), including 48/48 with all four defenses. It checks label agreement for A2, not identical text, independent human scoring or forged-figure repeatability.
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

`RESULTS-PRELIMINARY.csv` contains 24 model-condition rows and 12 pooled attack-group rows. `make-evidence-table.py` checks their arithmetic and prints the two main tables. [RESULTS-SUPPORTING.csv](RESULTS-SUPPORTING.csv) contains 58 additional aggregate rows for usefulness, adapted BIPIA, and A2 repeat agreement by model, defense and mode, plus temperature counts and changed-label directions. Its `count` and `denominator` apply to the stated metric; rows describe overlapping views and must not be added across scopes. BIPIA also records excluded retrieval cases and execution errors. These tables were checked separately against the recorded aggregates and repeat files; the supplied script only recomputes the original 36-row CSV. `EVIDENCE-SHA256.txt` records the bytes in this evidence package; these are post-run publication fingerprints, not preregistration.

Tables and this note: CC BY 4.0. Table-generation script: MIT. Published 4 October 2026. These hashes are post-run publication fingerprints, not preregistration.

Update, 4 October 2026: added the post-hoc grouping, usefulness and adapted-BIPIA counts, A2 repeat details, and the 13/24 CSV answer outcome separately from 24/24 retrieval. No new experiment was run and the original 36 CSV rows are unchanged.

Further method detail, 4 October 2026: expanded BIPIA to all six defenses and recorded scorer, exclusions, repeat settings and both temperatures. Added the machine-readable supporting CSV after checking the datatest handoff. This does not publish defense code or raw answers.

Update, 8 October 2026: reordered the main finding to lead with the document-injection comparison before the sanitizer side effect. No counts changed.

# Third-party tools and datasets

Versions and licenses read from the installed packages on the test machine on 2026-09-28; BIPIA and LLMail-Inject licenses read from their upstream LICENSE file and dataset card on 2026-10-01.

| Name | Version | License | Note |
|---|---|---|---|
| garak (NVIDIA) | 0.17.0 | Apache-2.0 | from `garak-0.17.0.dist-info/METADATA` |
| promptfoo | 0.123.1 | MIT | from `node_modules/promptfoo/LICENSE`; not used for results: it contacted its vendor's cloud despite opt-out settings, so it was excluded (documented in the report) |
| PyRIT (Microsoft) | 1.1.0 | MIT | from `pyrit-1.1.0.dist-info/METADATA` |
| BIPIA (Microsoft) | repository main branch (commit recorded at release) | MIT (code) |  only IDs and hashes are used, no text (table data is CC BY-SA) |
| LLMail-Inject (Microsoft) | Hugging Face dataset `microsoft/llmail-inject-challenge` | MIT (dataset card) |  fixed sample, seed recorded |

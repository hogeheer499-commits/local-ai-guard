#!/usr/bin/env python3
"""Recompute preliminary evidence tables from aggregates; no model tests run.

SPDX-License-Identifier: MIT
Copyright (c) 2026 hogeheer499-commits
"""
from pathlib import Path
import csv
from collections import defaultdict

ORDER = ['none', 'prompt', 'sanitize', 'link_filter', 'provenance', 'all']
ROWS = list(csv.DictReader((Path(__file__).parent / 'RESULTS-PRELIMINARY.csv').open()))
model_rows = [r for r in ROWS if r['scope'] == 'per_model']
pooled = [r for r in ROWS if r['scope'] == 'pooled_attack_group']
assert len(model_rows) == 24 and len(pooled) == 12
assert len({(r['model'], r['defense']) for r in model_rows}) == 24
assert {r['defense'] for r in model_rows} == set(ORDER)
for row in ROWS:
    for suffix in ['', '_without_a10']:
        k = int(row['successes' + suffix]); n = int(row['attempts' + suffix])
        assert 0 <= k <= n
totals = defaultdict(lambda: [0, 0, 0, 0])
for row in model_rows:
    acc = totals[row['defense']]
    acc[0] += int(row['successes']); acc[1] += int(row['attempts'])
    acc[2] += int(row['successes_without_a10']); acc[3] += int(row['attempts_without_a10'])
print('| Defense | Instruction-related | Forged figures | Total |')
print('|---|---:|---:|---:|')
for defense in ORDER:
    parts = [r for r in pooled if r['defense'] == defense]
    assert len(parts) == 2
    assert sum(int(r['successes']) for r in parts) == totals[defense][0]
    assert sum(int(r['attempts']) for r in parts) == totals[defense][1]
    assert sum(int(r['successes_without_a10']) for r in parts) == totals[defense][2]
    assert sum(int(r['attempts_without_a10']) for r in parts) == totals[defense][3]
    ins = next(r for r in parts if r['attack_group'] == 'instruction_related')
    forged = next(r for r in parts if r['attack_group'] == 'forged_figures')
    print(f"| {defense} | {ins['successes']}/{ins['attempts']} | {forged['successes']}/{forged['attempts']} | {totals[defense][0]}/{totals[defense][1]} |")
print()
print('| Model | None | Prompt | Sanitizer | Links | Provenance | All four |')
print('|---|---:|---:|---:|---:|---:|---:|')
for model in sorted({r['model'] for r in model_rows}):
    values = {r['defense']: r['successes'] for r in model_rows if r['model'] == model}
    assert set(values) == set(ORDER)
    print('| ' + model + ' | ' + ' | '.join(values[d] for d in ORDER) + ' |')

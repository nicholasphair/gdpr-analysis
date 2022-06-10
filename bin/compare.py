#!/usr/bin/env python3

import csv
import json
from collections import Counter

folder = 'data'
MANUAL_ANALYSIS = 'ma.csv'
SYSTEM_ANALYSIS = f'{folder}/success.csv'
OUTPUT = f'{folder}/results.csv'
STATS = f'{folder}/stats.json'
COUNTS = f'{folder}/counts.json'
SYSTEM_COUNTS = f'{folder}/sa_counts.json'

VIOLATION_CATEGORIES = [
    'delete_violation',
    'access_violation',
    'third_party_violation',
    'encryption_violation',
    'violation',
]


def statistics(results):
    counts = Counter([f'{k} = {v}' for r in results.values() for k, v in r.items()])
    ptotals = Counter([k for r in results.values() for k, v in r.items() if 'FP' in v or 'TN' in v])
    ntotals = Counter([k for r in results.values() for k, v in r.items() if 'FN' in v or 'TP' in v])

    percents = {}
    for k, v in counts.items():
        split_key = k.split()
        tk = split_key[0]
        tv = split_key[-1]
        if tv == '=':
            continue

        totals = ptotals if 'FP' in tv or 'TN' in tv else ntotals
        percents[k] = v / totals[tk] * 100
    return percents


def process_results(results):
    stats = statistics(results)
    with open(STATS, 'w') as jsonfile:
        jsonfile.write(json.dumps(stats, indent=4, sort_keys=True))

    counts = Counter([f'{k} = {v}' for r in results.values() for k, v in r.items()])
    with open(COUNTS, 'w') as jsonfile:
        jsonfile.write(json.dumps(dict(counts), indent=4, sort_keys=True))

    with open(OUTPUT, 'w', newline='') as csvfile:
        fieldnames = ['name'] + VIOLATION_CATEGORIES
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for k, v in results.items():
            v['name'] = k
            writer.writerow(v)


def is_violation(result):
    return result == 'true'


def categorizable(man, sys):
    return man and sys


def categorize(man, sys):
    if not categorizable(man, sys):
        return ''

    if is_violation(sys):
        return 'TP' if is_violation(man) else 'FP'
    else:
        return 'TN' if not is_violation(man) else 'FN'


def analyze(man_analysis, sys_analysis):
    result = {}
    for vc in VIOLATION_CATEGORIES:
        ground_truth = man_analysis.get(vc, '')
        sys_result = sys_analysis.get(vc, '')
        result[vc] = categorize(ground_truth, sys_result)
    return result


def system_only():
    with open(SYSTEM_ANALYSIS, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        system = {record['name']: record for record in reader}

    violations = dict(Counter([f'{k}={v}' for x in system.values() for k, v in x.items() if k != 'name']))
    violations['total'] = len(system)
    with open(SYSTEM_COUNTS, 'w') as jsonfile:
        jsonfile.write(json.dumps(violations, indent=4, sort_keys=True))


def run_analysis():
    with open(MANUAL_ANALYSIS, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        manual = {record['name']: record for record in reader}

    with open(SYSTEM_ANALYSIS, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        system = {record['name']: record for record in reader}

    results = {}
    for k, v in system.items():
        man = manual.get(k)
        if not man:
            print(f'could not find manual results for {k}')
            continue
        results[k] = analyze(man, v)

    return results


system_only()
results = run_analysis()
process_results(results)

import json
import subprocess
import sys

def test_cases(cases):
    with open('_test_temp.json', 'w', encoding='utf-8') as f:
        json.dump(cases, f, indent=2)
    res = subprocess.run(['cargo', 'run', '-p', 'kiteo-runner', '--', '--file', '_test_temp.json'], capture_output=True, text=True)
    print(res.stdout)
    if res.stderr and 'error' in res.stderr.lower():
        print("STDERR:", res.stderr[-500:])

if __name__ == '__main__':
    from corpus_part1 import PART1_CASES
    print(f"Testing first 4 cases of part 1...")
    test_cases(PART1_CASES[:4])

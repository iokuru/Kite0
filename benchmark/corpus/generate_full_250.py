import json
import os
import sys

sys.path.insert(0, os.getcwd())

# 1. Base existing 40 problems (80 cases)
existing_path = os.path.join(os.path.dirname(__file__), "tough_benchmark.json")
with open(existing_path, "r", encoding="utf-8") as f:
    existing_cases = json.load(f)

base_cases = existing_cases[:80]
print(f"Loaded {len(base_cases)} base cases ({len(base_cases)//2} distinct problems: 1 to 40).")

# 2. Part 1 (Problems 41 to 90 = 50 problems, 100 cases)
from benchmark.corpus.corpus_part1 import PART1_CASES
print(f"Loaded {len(PART1_CASES)} part 1 cases ({len(PART1_CASES)//2} problems: 41 to 90).")

# 3. Part 2 (Problems 91 to 145 = 55 problems, 110 cases)
from benchmark.corpus.corpus_part2 import PART2_CASES
print(f"Loaded {len(PART2_CASES)} part 2 cases ({len(PART2_CASES)//2} problems: 91 to 145).")

# 4. Part 3 (Problems 146 to 195 = 50 problems, 100 cases)
from benchmark.corpus.corpus_part3 import PART3_CASES
print(f"Loaded {len(PART3_CASES)} part 3 cases ({len(PART3_CASES)//2} problems: 146 to 195).")

# 5. Part 4 (Problems 196 to 250 = 55 problems, 110 cases)
from benchmark.corpus.corpus_part4 import PART4_CASES
print(f"Loaded {len(PART4_CASES)} part 4 cases ({len(PART4_CASES)//2} problems: 196 to 250).")

full_cases = base_cases + PART1_CASES + PART2_CASES + PART3_CASES + PART4_CASES

print(f"\nTotal combined cases: {len(full_cases)}")
assert len(full_cases) == 500, f"Expected 500 cases, got {len(full_cases)}"

# Validation checks
ids = [c["id"] for c in full_cases]
assert len(ids) == len(set(ids)), f"Duplicate IDs found! Total {len(ids)}, unique {len(set(ids))}"

cpp_count = sum(1 for c in full_cases if c["language"] == "cpp")
java_count = sum(1 for c in full_cases if c["language"] == "java")
assert cpp_count == 250, f"Expected 250 cpp cases, got {cpp_count}"
assert java_count == 250, f"Expected 250 java cases, got {java_count}"

# Check matching pairs
cpp_bases = {c["id"].replace("_cpp", "") for c in full_cases if c["language"] == "cpp"}
java_bases = {c["id"].replace("_java", "") for c in full_cases if c["language"] == "java"}
assert cpp_bases == java_bases, f"Mismatch between C++ and Java problem bases!"
assert len(cpp_bases) == 250, f"Expected 250 distinct problem bases, got {len(cpp_bases)}"

print(f"All validation checks PASSED: 250 distinct problems, 500 cases (250 C++, 250 Java).")

# Write to tough_benchmark.json
with open(existing_path, "w", encoding="utf-8") as f:
    json.dump(full_cases, f, indent=2)

print(f"Successfully saved full 250-problem suite (500 cases) to {existing_path}!")

# https://rosalind.info/problems/dna/

# multiple solutions provided:

# 1. Using dict comprehension

from collections import defaultdict 
count = defaultdict(int, {s: count[s]+1 for s in dataset})

# 2. Using simple defaultdict

from collections import defaultdict 
counts = defaultdict(int)
for c in dataset:
  counts[c] += 1

# 3. Using counter

from collections import Counter
counts = Counter(dataset)


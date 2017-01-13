# Author: Mitchell Fehr
# Date: 10/24/16
#
# "Making Anagrams" Solution

from collections import Counter

counts = Counter(input())
counts.subtract(input())
print(sum(abs(x) for x in counts.values()))

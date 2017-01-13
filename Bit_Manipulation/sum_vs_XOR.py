# Author: Mitchell Fehr
# Date: 10/27/16
#
# "Sum vs XOR" Solution

import sys


n = int(input().strip())
count = 0
for x in range(n+1):
    if n ^ x == x+n:
        count += 1
        print(bin(x))
        print(x)
print(count)

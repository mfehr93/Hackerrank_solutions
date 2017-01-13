# Author: Mitchell Fehr
# Date: 10/24/2016
#
# "Alternating Characters" Solution

import sys

n = int(input().strip())
for i in range(n):
    count = 0
    s = input().strip()
    for j in range(len(s)-1):
        if s[j]==s[j+1]:
            count += 1
    print(count)

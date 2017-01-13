# Author: Mitchell Fehr
# Date: 10/24/2016
#
# "The Love-Letter Mystery" Solution

import sys

t = int(input().strip())
for _ in range(t):
    ops = 0
    s = input().strip()
    for i in range(len(s)//2):
        ops += abs(ord(s[i])-ord(s[-(i+1)]))
    print(ops)

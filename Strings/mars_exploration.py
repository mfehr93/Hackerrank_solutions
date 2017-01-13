# Author: Mitchell Fehr
# Date: 10/24/2016
#
# "Mars Exploration" Solution

import sys

sRec = input().strip()
n = len(sRec)
sExp = 'SOS'*(n//3)
count = 0
for i in range(n):
    if sRec[i]!=sExp[i]:
        count += 1
print(count)

# Author: Mitchell Fehr
# Date: 10/16/2016
#
# "The Maximum Subarray" solution

import sys
t = int(input().strip())
out = ''
maxOf = dict()
for i in range(t):
    n = int(input().strip())
    a = list(map(int,input().strip().split(' ')))
    maxEndingHere = maxSoFar = a[0]
    if a[0] > 0:
        totNC = a[0]
    else:
        totNC = 0
    for x in a[1:]:
        maxEndingHere = max(x,maxEndingHere + x)
        maxSoFar = max(maxSoFar,maxEndingHere)
        if x > 0:
            totNC += x
    if totNC == 0:
        totNC = max(a)
    
    out += str(maxSoFar) + ' ' + str(totNC) + '\n'
print(out)

# Author: Mitchell Fehr
# Date: 10/5/2016
#
# "Sock Merchant" Python 3 Solution

import sys
n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

d = dict()
pairs = 0

for sock in c:
    if sock in d:
        d[sock] = d[sock]+1
    else:
        d[sock] = 1
        
for key in d:
    pairs += d[key] // 2
    
print(pairs)

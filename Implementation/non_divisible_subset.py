# Author: Mitchell Fehr
# Date: 10/5/2016
#
# "Non-Divisible Subset" Python 3 Solution

import sys
n, k = map(int,input().strip().split(" "))
s = map(int,input().strip().split(" "))

def sub(n,k,s):
    d = [0]*k
    for num in s:
        d[num % k] +=1
    tot = min(d[0],1)
    for i in range(1,(k//2)+1):
        if i != (k - i):
            tot += max(d[i],d[k-i])
    if k % 2 == 0:
        tot +=1
    print(tot)


sub(n,k,s)
            
        
        

# Author: Mitchell Fehr
# Date: 10/14/2016
#
# "CircularArrayRotation" Python 3 Solution

#!/bin/python3

import sys


n, k, q = input().strip().split(' ')
n = int(n)
k = int(k)
q = int(q)
k = k % n


arr = [int(i) for i in input().strip().split(' ')]
arr2 = []
for i in range(q):
    m = int(input())
    arr2.append(arr[(m-k)%n])
for i in range(len(arr2)):
    print(arr2[i])




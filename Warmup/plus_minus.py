# Author: Mitchell Fehr
# Date: 10/14/2016
#
# "DiagonalDifference" Python 3 Solution

#!/bin/python3

import sys

n = int(input().strip())
arr = []
for i in range(n):
    arr.append([int(arr_temp) for arr_temp in input().strip().split(' ')])

def diagDiff(arr):
    d1, d2 = (0,0)
    for i in range(n):
        d1 += arr[i][i]
        d2 += arr[i][-(i+1)]
    print(abs(d1-d2))

diagDiff(arr)

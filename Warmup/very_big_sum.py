# Author: Mitchell Fehr
# Date: 10/14/2016
#
# "CompareTheTriplets" Python 3 Solution

#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
m = 0
for i in arr:
    m += i
print(m)


# Author: Mitchell Fehr
# Date: 10/14/2016
#
# "CompareTheTriplets" Python 3 Solution

import sys

a0,a1,a2 = [int(i) for i in input().strip().split(' ')]
b0,b1,b2 = [int(i) for i in input().strip().split(' ')]
alice = 0
bob = 0

if a0 < b0:
    bob += 1
elif a0 > b0:
    alice += 1
if a1 < b1:
    bob += 1
elif a1 > b1:
    alice += 1
if a2 < b2:
    bob += 1
if a2 > b2:
    alice += 1
print(str(alice) + ' ' +str(bob))

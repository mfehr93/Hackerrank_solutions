# Author: Mitchell Fehr
# Date: 10/20/2016
#
# "Counting Sort 1" Python 3 Solution

n = int(input().strip())
arr = list(map(int,input().strip().split()))

def count(n,arr):
    l = [0 for i in range(100)]
    for x in arr:
        l[x] += 1
    s = str(l[0])
    for i in range(1,100):
        s += ' ' + str(l[i])
    print(s)

count(n,arr)

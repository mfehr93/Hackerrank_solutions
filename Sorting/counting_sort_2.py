# Author: Mitchell Fehr
# Date: 10/20/2016
#
# "Counting Sort 2" Python 3 Solution

n = int(input().strip())
arr = list(map(int,input().strip().split()))

def count(n,arr):
    l = [0 for i in range(100)]
    for x in arr:
        l[x] += 1
    s = str(l[0])
    for i in range(1,100):
        s += ' ' + str(l[i])
    return s

def sort(n,arr):
    s = count(n,arr)
    l = list(map(int,s.strip().split(' ')))
    out = ''
    for i in range(100):
        out += l[i]*(str(i)+' ')
    print(out)

sort(n,arr)

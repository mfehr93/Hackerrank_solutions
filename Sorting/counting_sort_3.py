# Author: Mitchell Fehr
# Date: 10/20/2016
#
# "Counting Sort 3" Python 3 Solution

n = int(input().strip())
l = []
for _ in range(n):
    x,s = list(input().strip().split(' '))
    l.append(int(x))

def count(n,arr):
    l = [0 for i in range(100)]
    for x in arr:
        l[x] += 1
    count = l[0]
    s = str(count)
    for i in range(1,100):
        count += l[i]
        s += ' ' + str(count)
    print(s)

count(n,l)

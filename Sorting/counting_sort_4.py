# Author: Mitchell Fehr
# 10/20/2016
#
# "The Full Counting Sort" Solution

def count(n,arr):
    l = [0 for i in range(100)]
    for x,s in arr:
        l[x] += 1
    count = l[0]
    s = str(count)
    for i in range(1,100):
        count += l[i]
        s += ' ' + str(count)
    return(l)

n = int(input().strip())
arr = []
arr2 = [[] for _ in range(100)]
c = 0
for _ in range(n):
    (x,s) = input().strip().split(' ')
    if c < n//2:
        arr.append((int(x),'-'))
        arr2[int(x)].append('-')
    else:
        arr.append((int(x),s))
        arr2[int(x)].append(s)
    c += 1
l = count(n,arr)
s = ''
for i in range(100):
    for j in range(l[i]):
        s += arr2[i][j] + ' '
print(s)

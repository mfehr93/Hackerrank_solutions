# Author: Mitchell Fehr
# 10/20/2016
#
# "Running Time of Algorithms" Solution

def insertion_sort(l):
    count = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           count += 1
        l[j+1] = key
    print(count)

m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)

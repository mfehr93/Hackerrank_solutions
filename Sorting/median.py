# Author: Mitchell Fehr
# 10/22/2016
#
# "Find the Median" Solution

n = int(input().strip())
arr = [int(i) for i in input().strip().split()]

def partition(arr,lo,hi):
    p = arr[hi]
    i = lo
    for j in range(lo,hi):
        if arr[j] <= p:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1
    temp = arr[i]
    arr[i] = p
    arr[hi] = temp
    return(i)

def median(arr,n):
    med = n//2
    i = partition(arr,0,n-1)
    while i != med:
        if i < med:
            i = median(arr[:i],i)
        elif i > med:
            i = median(arr[i:],n-i)
    print(arr[i])

median(arr,n)

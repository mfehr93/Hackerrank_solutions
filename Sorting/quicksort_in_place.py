# Author: Mitchell Fehr
# 10/22/2016
#
# "Quicksort In-Place" Solution

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
    print(' '.join(map(str,arr)))
    return(i)

def quicksort(arr,lo,hi):
    if lo < hi:
        p = partition(arr,lo,hi)
        quicksort(arr,lo,p-1)
        quicksort(arr,p+1,hi)
    
quicksort(arr,0,n-1)

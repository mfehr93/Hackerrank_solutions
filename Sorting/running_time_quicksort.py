# Author: Mitchell Fehr
# 10/22/2016
#
# "Running Time of Quicksort" Solution

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
    return(count)

def partition(arr,lo,hi,countQS):
    p = arr[hi]
    i = lo
    for j in range(lo,hi):
        if arr[j] <= p:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            i += 1
            countQS += 1
    temp = arr[i]
    arr[i] = p
    arr[hi] = temp
    countQS += 1
    return(i,countQS)

def quicksort(arr,lo,hi,countQS):
    if lo < hi:
        p,countQS = partition(arr,lo,hi,countQS)
        countQS = quicksort(arr,lo,p-1,countQS)
        countQS = quicksort(arr,p+1,hi,countQS)
        return(countQS)
    return(countQS)
n = int(input().strip())
ar = [int(i) for i in input().strip().split(' ')]
ar1 = [i for i in ar]           #A silly copy of ar, so that we don't mutate the original ar
ins = insertion_sort(ar1)
q = quicksort(ar,0,n-1,0)
print(ins-q)

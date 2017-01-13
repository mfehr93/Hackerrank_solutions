# Author: Mitchell Fehr
# 10/20/2016
#
# "Quicksort 2 - Sorting" Solution

n = int(input().strip())
arr = [int(i) for i in input().strip().split()]

def partition(arr,n):
    p = arr[0]
    left = []
    equal = []
    right = []
    for i in range(n):
        if arr[i] < p:
            left.append(arr[i])
        elif arr[i] == p:
            equal.append(arr[i])
        else:
            right.append(arr[i])
    return(left,equal,right)

def quicksort(arr,n):
    if n < 2:
        return(arr)
    if n == 2:
        if arr[0] > arr[1]:
            arr = [arr[1],arr[0]]
        print(' '.join(map(str,arr)))
        return(arr)
    if n > 2:
        left,equal,right = partition(arr,n)
        left = quicksort(left,len(left))
        right = quicksort(right,len(right))
        print(' '.join(map(str,left+equal+right)))
        return(left+equal+right)
    
quicksort(arr,n)

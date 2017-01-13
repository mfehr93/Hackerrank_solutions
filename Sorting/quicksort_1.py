# Author: Mitchell Fehr
# 10/20/2016
#
# "Quicksort 1 - Partition" Solution

n = int(input().strip())
arr = [int(i) for i in input().strip().split()]

def quicksort(arr,n):
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
    print(' '.join(map(str,left+equal+right)))    
    
quicksort(arr,n)

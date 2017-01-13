# Author: Mitchell Fehr
# Date: 10/5/2016
#
# "Insertion Sort - Part 1" solution

import sys
n = int(input())
arr = list(input().strip().split(" "))

def insertSort(n, arr):
    x = arr[n-1]
    j = n-1
    while j > 0 and arr[j-1] > x:
        arr[j] = arr[j-1]
        s = arr[0]
        for i in range(1,n):
            s += ' '+arr[i]
        print(s)
        j = j - 1
    arr[j] = x
    s = arr[0]
    for i in range(1,n):
        s += ' '+arr[i]
    print(s)
            
insertSort(n,arr)
        

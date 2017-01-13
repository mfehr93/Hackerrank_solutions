# Author: Mitchell Fehr
# Date: 10/5/2016
#
# "Insertion Sort - Part 2" solution

import sys
n = int(input())
strArr = list(input().strip().split(" "))
arr = []
for item in strArr:
    arr.append(int(item))

def insertSort(n, arr):

    for i in range(1,n):
        x = arr[i]
        j = i
        while j > 0 and arr[j-1] > x:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = x
        s = str(arr[0])
        for i in range(1,n):
            s += ' '+str(arr[i])
        print(s)
            
insertSort(n,arr)
        

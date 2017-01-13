# Author: Mitchell Fehr
# 10/20/2016
#
# "Closest Numbers" Solution

n = int(input().strip())
arr = list(map(int,input().strip().split(' ')))

def closest(n,arr):
    arr = sorted(arr)
    minDist = 2*(10**7)+1
    closest = ''
    for i in range(n-1):
        dist = abs(arr[i]-arr[i+1])
        if dist < minDist:
            minDist = dist
            closest = str(arr[i]) + ' ' + str(arr[i+1])
        elif dist == minDist:
            closest += ' ' + str(arr[i]) + ' ' + str(arr[i+1])
    print(closest)

closest(n,arr)

# Author: Mitchell Fehr
# Date: 10/22/2016
#
# "Intro to Tutorial Challenges" Solution

v = int(input().strip())
n = int(input().strip())
ar = [int(i) for i in input().strip().split(' ')]

def find(ar,n,v):
    for i in range(n):
        if ar[i] == v:
            print(i)

find(ar,n,v)

# Author: Mitchell Fehr
# Date: 1/7/17
#
# "The Coin Change Problem" solution

import sys

n, m = list(map(int,input().strip().split(' ')))
c = list(map(int,input().strip().split(' ')))
c.sort(reverse=True)
calculated = [[False]*252 for y in range(53)]
table = [[0]*252 for y in range(53)]

def solve(i,amt):
    if amt<0 :
        return(0)
    elif (amt == 0):
        return(1)
    elif (calculated[i][amt]==False)& (i<m):
        table[i][amt] = solve(i,amt-c[i]) + solve(i+1,amt)
        calculated[i][amt]=True
    return(table[i][amt])

print(solve(0,n))

    
    

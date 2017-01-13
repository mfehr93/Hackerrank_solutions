# Author: Mitchell Fehr
# Date: 10/24/2016
#
# "Funny String" Solution

import sys

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    r = s[::-1]
    funny = 'Funny'
    for i in range(len(s)-1):
        if abs(ord(s[i])-ord(s[i+1]))!=abs(ord(r[i])-ord(r[i+1])):
            funny = 'Not Funny'
    print(funny)

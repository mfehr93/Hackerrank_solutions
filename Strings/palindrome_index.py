# Author: Mitchell Fehr
# Date: 10/25/2016
#
# "Palindrome Index" Solution

import sys

n = int(input().strip())
for _ in range(n):
    found = False
    s = input().strip()
    for i in range(len(s)-1):
        if s[i]!=s[-(i+1)]:
            if s[i+1]==s[-(i+1)]:
                print(i)
                found = True
                break
            elif s[i]==s[-(i+2)]:
                print(len(s)-i-1)
                found = True
                break
    if not found:
        print(-1)

# Author: Mitchell Fehr
# Date: 10/27/16
#
# "Lonely Integer" Solution

n,ar = int(input().strip()),[int(x) for x in input().strip().split(' ')]
ans = 0
for x in ar:
    ans = ans^x
print(ans)

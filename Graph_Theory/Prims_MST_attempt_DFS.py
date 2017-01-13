# Author: Mitchell Fehr
# Date: 10/5/2016
#
# Prim's Algorithm for MST solution

import sys
nodes = dict()
visited = set()
notvisited = set()
total = 0
nn, mm = input().strip().split(" ")
n = int(nn)
m = int(mm)

for i in range(1,n+1):
    nodes[i] = []
    notvisited.add(i)
for i in range(1,m+1):
    xx, yy, rr = input().strip().split(" ")
    x = int(xx)
    y = int(yy)
    r = int(rr)
    nodes[x].append((y,r))
    nodes[y].append((x,r))
s = int(input())
visited.add(s)
nmin = 0
while len(notvisited) > 0:
    wmin = 10**5 + 1
    for (s2,w) in nodes[s]:
        if s2 not in visited:
            if wmin > w:
                nmin = s2
                wmin = w
    if wmin == 10**5 + 1:
        s = notvisited.pop()
    else:
        total += wmin
        visited.add(s)
        s = nmin
        notvisited.discard(s)

print(total)


    

# Author: Mitchell Fehr
# Date: 10/5/2016
#
# Prim's Algorithm for MST solution

import sys
nodes = dict()
orig = set()
new = set()

total = 0
nn, mm = input().strip().split(" ")
n = int(nn)
m = int(mm)

for i in range(1,n+1):
    nodes[i] = []
    orig.add(i)
for i in range(1,m+1):
    xx, yy, rr = input().strip().split(" ")
    x = int(xx)
    y = int(yy)
    r = int(rr)
    nodes[x].append((y,r))
    nodes[y].append((x,r))
s = int(input())
new.add(s)
orig.remove(s)
nmin = 0
while len(orig) > 0:
    wmin = 10**5 + 1
    for vertex in new:
        for (s2,w) in nodes[vertex]: # min can currently be visited
            if w < wmin and s2 in orig:
                wmin = w
                nmin = s2
    total += wmin
    orig.discard(nmin)
    new.add(nmin)
    

print(total)


    

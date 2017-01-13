# Author: Mitchell Fehr
# Date: 10/20/2016
#
# "Grid Challenge" Python 3 Solution
# NOTE:: we do not take a greedy approach, here.

def grid():
    t = int(input().strip())
    count = 0
    while count < t:
        g = []
        n = int(input().strip())
        out = "YES"
        for i in range(n):
            g.append(sorted(input().strip()))
        for j in range(n):
            for k in range(n-1):
                if g[k][j]>g[k+1][j]:
                    out = "NO"
        print(out)
        count += 1

grid()


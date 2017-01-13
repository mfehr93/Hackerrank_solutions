# Mitchell Fehr
# 1/10/17
#
# "Vertical Sticks" Problem
#
# This problem utilizes the "linearity of expectation" for its solution.

def main():
    T = int(input())
    for i in range(T):
        m = int(input())
        Y = list(map(int,input().strip().split()))
        solve(m,Y)
        
def solve(m,Y):
    Y.sort()
    p = 1
    prev = Y[0]
    prevInd = 0
    for i in range(1,len(Y)):
        if prev == Y[i]:
            p += (m+1)/(m-prevInd+1)
        else:
            p += (m+1)/(m-i+1)
            prev = Y[i]
            prevInd = i
    print("%.2f" % p)

main()

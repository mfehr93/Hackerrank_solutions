# Author: Mitchell Fehr
# Date: 10/5/2016
#
# "Super Reduced String" Python 3 Solution

'''
'''
def redString(s):
    n = len(s)
    for i in range(n-1):
        if s[i]==s[i+1]:
            return redString(s[0:i]+s[(i+2):n])
    if n==0:
        print("Empty String")
    else:
        print(s)

def main():
    inp = input()
    redString(inp)

main()

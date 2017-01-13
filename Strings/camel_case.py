# Author: Mitchell Fehr
# Date: 10/5/2016
#
# "camelCase" Python 3 Solution

import sys

def camelCase(s):
    i = 1
    for letter in s:
        if ord(letter) < 97:
            i += 1
    print(i)
            

def main():
    return camelCase(input().strip())

main()

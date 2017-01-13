# Author: Mitchell Fehr
# Date: 10/5/2016
#
# "Two Characters" exercise

s_len = int(input().strip())
s = input().strip()
chars = set(s)
def reduceString(s):
    chars = {}
    for char in s:
        chars.add(char)
    chars1 = chars
    #for char in chars

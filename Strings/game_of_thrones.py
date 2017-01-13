# Author: Mitchell Fehr
# Date: 10/25/16
#
# "Game of Thrones" Solution

s = input().strip()

st = set(s)
d = dict([(c,0) for c in st])
for char in s:
    d[char] += 1
someOdd = 0
out = 'YES'
for key in d:
    if d[key] % 2 != 0:
        if someOdd == 1:
            out = 'NO'
        else:
            someOdd = 1
print(out)

# Author: Mitchell Fehr
# Date: 10/24/16
#
# "Two Strings" Solution

p = int(input().strip())
for _ in range(p):
    a,b = input().strip(),input().strip()
    sa,sb = set(a),set(b)
    if len(sa.intersection(sb))>0:
        print('YES')
    else:
        print('NO')

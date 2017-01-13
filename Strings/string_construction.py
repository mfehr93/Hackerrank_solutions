# Author: Mitchell Fehr
# Date: 10/24/2016
#
# "String Construction" Solution

import sys

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    st = set(s[0])
    cost = 1
    for i in range(1,len(s)):
        if s[i] not in st:
            st.add(s[i])
            cost += 1
    print(cost)

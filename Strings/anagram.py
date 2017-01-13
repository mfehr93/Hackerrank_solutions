# Author: Mitchell Fehr
# Date: 10/24/16
#
# "Anagram" Solution

t = int(input().strip())
for _ in range(t):
    s = input().strip()
    length = len(s)
    d = dict()
    if length % 2 != 0:
        print(-1)
    else:
        l = len(s)//2
        s1,s2 = s[:l],s[l:]
        d1,d2 = dict(),dict()
        for i in range(l):
            if s1[i] in d1:
                d1[s1[i]] += 1
            else:
                d1[s1[i]] = 1
            if s2[i] in d2:
                d2[s2[i]] += 1
            else:
                d2[s2[i]] = 1
        count = 0
        for key in d1:
            if key in d2:
                count += abs(d1[key] - d2[key])
            else:
                count += d1[key]
        for key in d2:
            if key not in d1:
                count += d2[key]
        print(count//2)
            

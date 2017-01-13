# Author: Mitchell Fehr
# Date: 10/23/2016
#
# "Pangrams" Solution

s = input().strip()

def pangrams(s):
    st = set()
    for i in range(97,123):
        st.add(chr(i))
        st.add(chr(i-32))
    for c in s:
        st.discard(c)
        n = ord(c)
        if n <= 90:
            st.discard(chr(n+32))
        else:
            st.discard(chr(n-32))
    if len(st) == 0:
        print('pangram')
    else:
        print('not pangram')

pangrams(s)

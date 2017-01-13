# Author: Mitchell Fehr
# Date: 10/14/2016
#
# "TimeConversion" Python 3 Solution

#!/bin/python3

import sys

hr, mn, sec = input().strip().split(':')
ampm = sec[2:]
sec = sec[:2]

if ampm == 'AM':
    if hr != '12':
        print(hr + ':' + mn + ':' + sec)
    else:
        print('00:' + mn + ':' + sec)
elif ampm == 'PM':
    if hr != '12':
        hr = str(int(hr) + 12)
        print(hr + ':' + mn + ':' + sec)
    else:
        print(hr + ':' + mn + ':' + sec)

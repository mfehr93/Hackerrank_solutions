# Author: Mitchell Fehr
# Date: 10/14/2016
#
# "Staircase" Python 3 Solution

#!/bin/python3

import sys

size = int(input().strip())

for i in range(size):
    print(' '*(size-i-1)+(i+1)*'#')

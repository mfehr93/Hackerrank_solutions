# Author: Mitchell Fehr
# Date: 10/14/2016
#
# "SimpleArraySum" Python 3 Solution

import sys

def simpleArraySum(nums):
    total = 0
    for num in nums:
        total += num
    return(total)
            
def main():
    size = input().strip()
    nums = [int(i) for i in input().strip().split(' ')]
    print(simpleArraySum(nums))

main()

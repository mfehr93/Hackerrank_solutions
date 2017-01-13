# Author: Mitchell Fehr
# Date: 10/5/2016
#
# "Fibonacci Modified" Python 3 Solution

import re

''' fib(t_1,t_2,n) = t_n
    Given t_1 and t_2, the first two terms, computes t_n,
    defined by the equation t_(i+2) = t_i + (t_(i+1))**2
    
'''

def fib(t1,t2,n):
    f = dict()
    f[1] = t1 # 0 
    f[2] = t2 # 1
    i = 3
    while i<=n: # while 3 < 5
        f[i] = f[i-2] + f[i-1]**2 #0 + 1^2
        i += 1
    print(f[n])
    return f[n]

def main():
    inp = input()
    nums = re.findall("[0-9]+",inp)
    fib(int(nums[0]),int(nums[1]),int(nums[2]))
    
main()
    
    
    

# Author: Mitchell Fehr
# Date: 10/20/2016
#
# "Luck balance" Python 3 Solution


def luck():
    n,k = map(int,input().strip().split(' '))
    luck = 0
    contests = []
    
    for _ in range(n):
        contests.append(list(map(int,input().split())))
    
    nonImportant = [x[0] for x in contests if x[1] == 0]
    important = sorted([x[0] for x in contests if x[1] == 1], reverse=True)
    luck = sum(nonImportant) + sum(important[:k]) - sum(important[k:])
    print(luck)
luck()

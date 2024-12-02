# ---Day 2---
input = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

import copy
total = 0

def safecheck(list):
    if list == sorted(list,key=int) or list == sorted(list,key=int,reverse=True):
        init = int(list[0])
        for i in range(1,len(list)):
            if abs(int(list[i])-init)<1 or abs(int(list[i])-init)>3:
                return False
            init = int(list[i])
        return True
    return False

def safecheck2(list):
    for i in range(len(list)):
        x = copy.deepcopy(list)
        x.pop(i)
        if safecheck(x) ==True:
            print(x)
            return True
    return False

for row in input.split('\n'):
    row = row.split()
    if safecheck(row) == True:
        total += 1

    #---part2---
    elif safecheck2(row) == True:
        total += 1
            
print(total)

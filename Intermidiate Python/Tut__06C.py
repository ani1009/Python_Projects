''' Reduce Function''' #--->  It Applies Chain Of Functions in a List.

from functools import reduce

def sum_num(a,b):
    return a+b

lis1 = reduce(sum_num, [1,2,3,4,5,7,9])

print(lis1)


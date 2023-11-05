# bisect --> Tells in Which no of Index Should we Insert a Number in Given List.
# insort --> Actually Insert the Given Number in a Given List & Updates List Including that Number.

import bisect

Number = 9

a = [1,2,5,6,8,10,12,15]

print(bisect.bisect(a, Number))

bisect.insort(a, Number)
print(a)


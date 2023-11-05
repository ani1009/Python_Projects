#1.List Comprehensions -

list_1 = [20,22,3,2,34,373,4,45,4383,33,11,34,37,27,21,9]
divide_by_3 = []

for item in list_1:
    if item % 3 ==0:
        divide_by_3.append(item)

print(divide_by_3) # Without Using List Comprehension,

print([item for item in list_1 if item % 3 == 0]) # Using List Comprehension.

#2.Dictionary Comprehensions -

dict1 = {'a':45, 'b':98, 'A':64}
print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

#3.Set Comprehensions -

squared = {x**2 for x in [1,2,2,3,4,4,5,5,6,7,8,9,9,10]}
print(squared)

#4.Generator Comprehensions -

gen = ( i for i in range(69) if i % 3 == 0)
for item in gen:
    print(item)


list1 = [["hp", 2],["mac", 4],["lenovo", 6],["acer", 3],["vaio", 1]]

dict1 = dict(list1)
print(dict1)

for item, parts in list1:
   print(item, parts)

for item, parts in dict1.items():
    print(item, parts)
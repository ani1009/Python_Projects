s = set()
'''print(type(s))
l =[1,2,3,4,5]
s_from_list = set(l)
print(type(s_from_list))'''

s.add(1)
s.add(2)
s.add(3)
s.add(1)

print(s)

s1 = s.union({1,2,3,4})
print(s1)

s2 = s.intersection({1,2,3,4})
print(s2)

set2 ={3,6,9}
print(s.isdisjoint(set2))

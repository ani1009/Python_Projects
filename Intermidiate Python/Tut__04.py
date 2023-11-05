# Iterable:- It is a Object that Gives Iterator.(String Objects are Iterable but Integers are not.)
# Iterator:- It is a Object that Defines Next Method.(Switch to Next Element.)
# Iteration:- To Iterate Something Or To Fetch its Next Elements Called as Iteration.

# Generator:- It is a Iterator Which We Can Iterate Only Once. i.e. To Generate Value From It Only at Once.

def gen (n):
    for i in range (n):
        yield i

print(gen(10000000))

#for i in gen (10000):
#    print(i)

Ob1 = gen (5)
'''print(next(Ob1))
print(next(Ob1))
print(next(Ob1))
print(next(Ob1))
print(next(Ob1))
print(next(Ob1))
'''
Num = "Aniket"
iter1 = iter(Num)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))

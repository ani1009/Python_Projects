# Lambda Functions:- # Syntax:---> lambda argument : manipulate(argument)

'''def Add(a,b):
    s = a+b
    return s'''

Add = lambda x, y : x + y  
print(Add(9,8))

Sub = lambda p, q : p - q
print(Sub(18,7))

Mul = lambda a, b : a * b
print(Mul(7,9))

Div = lambda m, n : m / n
print(Div(12,4))

Var = lambda j, k : j > k
print(Var(99,75))

# List Sorting By Lambda Function:-

def  x (val):
    return val[1]
a = [(1,2), (45,54), (78,877)]

#a.sort(key=lambda x: x[1])
a.sort(key=x)

print(a)

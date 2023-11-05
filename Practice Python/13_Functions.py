a = 64
b = 86

c = sum((a,b)) # Built in Functions
print(c)

def function1(a,b):
    print("Hello, Value Of Your Function is", a + b )

function1(7,5)

def function2(a,b):
    average = (a + b)/2
    """ This is a Function Which Calculates Average Of Two Numberes. """
    #print(average)
    return average

v = function2(10,20)
print(v)

print(function2.__doc__)


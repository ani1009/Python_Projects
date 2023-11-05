# *args and **kwargs Tutorial--> Generally For One Value, & Passes [List Values]
# *vars and **kvars Tutorial--> For Key,Value Pairs, & Passes {Dictionary Values}

# First Example:-(*args)
'''def function_01(name, age, rollno):
    print( "The name Of Student is" , name, "and His age is" , age, "Also rollno is" , rollno )

function_01("Aniket", 24, 1009)'''

def function_01(*args):
    print(type(args))
    
    print("The name Of Student is", args[0] , "and His age is", args[1] ,"Also rollno is", args[2])
    
#function_01("Aniket", 24, 1009)
lis = ["Aniket", 24, 1009]
#function_01(*lis)

# Second Example:-(**kwargs)

def printmarks(**kwargs):
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key, value)

Markslist = {"Aniket": 90, "Siddhesh": 88, "Shubham": 69, "Chaitanya": 75, "Deepraj":70 }
printmarks(**Markslist)

#(1+2-->Master):-
def master(normal, *args, **kwargs):
    print(normal)

    for i in args:
        print(i)

    for key,value in kwargs.items():
        print(key,value)

master("normal arg",*lis , **Markslist)


# 1. Calculate the Factorial Of the Given Number.
# 2. Find the Number Of Trailing Zeroes in that Factorial.

def Factorial(Number):
    if Number == 0 or Number == 1:
        return 1
    else:
        return Number * Factorial(Number - 1)

def factorialTrailingZeroes(Number):
    # 5! = 5*4*3*2*1 = 120 & (5*2=10 i.e. Trailing Zero is 1)
    # In Any No's Prime Factorization Trailing Zero Depends On 5
    Count = 0
    i = 5 
    # 100! = 100 // 5 + 100 // 5 * 5
    while(Number // i != 0):
        Count += int(Number / i)
        i = i * 5
        return Count
        
    '''Fact = Factorial(Number)
    print(Fact)
    Count = 0
    while(Fact % 10 ==0):
        Count = Count + 1
        Fact = Fact / 10
        return Count'''

if __name__ == "__main__":
   Number = int(input(" Enter the Number : \n "))
#Fact = Factorial(Number)

#print(f" Factorial Of Given Number is {Fact} ")

print(factorialTrailingZeroes(Number))


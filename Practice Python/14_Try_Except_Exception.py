print("Enter num 1:")
num1 = (input())

print("Enter num 2:")
num2 = (input())

try:
    print("The Sum Of These Two Numbers is", int(num1) + int(num2))

except Exception as e:
    print(e)

print("This Line is Very Important")
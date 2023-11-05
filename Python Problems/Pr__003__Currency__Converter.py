with open ('Currency_Data.txt') as f: 
    lines = f.readlines()

Currency_Dict = {}
for line in lines:
    parsed = line.split("\t")
    Currency_Dict[parsed[0]] = parsed[1]

Amount = int(input("Enter the Amount: \n"))

print("Enter the Name Of Currency that You Want to Convert this Amount to? & Available Options: \n ")

[print(item) for item in Currency_Dict.keys()]

Currency = input("Please Enter One Of These Currency Values: \n ")

print(f"{Amount} INR is Equal to {Amount*float(Currency_Dict[Currency])} {Currency}")






    


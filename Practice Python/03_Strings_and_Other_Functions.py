# String Slicing:-
mystr = "aniket is a good boy!"
print(len(mystr))

print(mystr[0:6])
print(mystr[:21])
print(mystr[:50]) # This Shows No Error But it Can Prints Upto Max Index

print(mystr[0:6:2])
print(mystr[::]) # print(mystr[0:21:1]) Shows Same String Slicing

print(mystr[::3])

# Negative Slicing:-
print(mystr[::-1]) # Reverse Returns a String
print(mystr[-4:-2]) # print(mystr[17:19]) Shows Same String Slicing

print(mystr[::-2])

print(mystr.isalnum()) # False--> Because Of Having Spaces in String Sentence
print(mystr.isalpha())
print(mystr.endswith("!"))
print(mystr.count("o"))
print(mystr.capitalize())
print(mystr.find("is"))
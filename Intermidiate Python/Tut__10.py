# Format Function:-

Users = ['Aniket','Siddhesh','Deepraj','Chaitanya','Shubham']

Mobiles =['Xiaomi','Motorolla','OnePlus','Samsung','Realme']

'''for i in range(0, len(Users)):
    print("Mobile Used by", Users[i],"is", Mobiles[i])'''

for i in range(0, len(Users)):

    Template = "Mobile Used by {} is {} "

print(Template.format(Users[i], Mobiles[i]))


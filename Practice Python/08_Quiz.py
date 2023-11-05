items = ["Veg","Nonveg",9,11,14,27,29,35,48,54]

for item in items:
    if str(item).isnumeric() and item >=9:
        print(item)
        
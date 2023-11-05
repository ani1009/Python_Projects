# Dictionary is Nothing But Key-Value Pairs.
d1 ={}
print(type(d1))

d2 = {"Aniket": "Pizza", "Sid": "Burger", "Deepya": "Vegetables",
        "Shubham":{"B":"Roti", "L":"Rice", "D":"Non-Veg"}}
d2 ["Chaitanya"] = "Juice"

d2[1009] = "Momos"
del d2["Chaitanya"]

print(d2)
print(d2["Sid"])

d3 = d2.copy()
del d2["Deepya"]
print(d2)

print(d2.get("Aniket"))
d2.update({"Hari":"Dahi"})
print(d2)

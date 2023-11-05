''' Filter Function''' #:->>> It Makes List Of Elements & 
# Filters List Of Elements For Which a Function Returns True.

def greater_than_2(n):
    if n>2:
        return True
    else:
        return False

m1 = [1,2,3,-4,-6,5,7,9,11]

greater_th_2 = list(filter(greater_than_2, m1))

print(greater_th_2)

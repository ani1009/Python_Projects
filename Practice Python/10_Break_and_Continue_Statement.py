i = 0

while (True):
    if i + 1 < 5:
        i = i + 1
        continue
    
    print(i+1, end = " ")
    if (i == 40):
        break # Stop the Loop
    i = i + 1

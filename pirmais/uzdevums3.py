

with open("item.txt", "w")as file:
    for i in range(100):
        file.write(f"Item \n ")
        file.write (str(i))



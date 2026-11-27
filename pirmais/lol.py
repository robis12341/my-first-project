while True:
    ievade = input("Ieraksti vardu: ")

    if ievade == "0":
        break

    print(ievade)

    with open("data.txt", "a") as file:
        file.write(ievade + "\n")                             
word = "computer"



for i in range(4):
    print(f'{i:02d}. {word}')

with open ('data.txt', "w" )as file:
    for i in range(26):
        file.write (f'{i:02d}. {word}\n ')

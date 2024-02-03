with open("file.txt","r",encoding="utf-8") as f:
    vowels = {"а","о","у","и","і","е"}
    vowels_counter = 0
    consostants_counter = 0
    number_counter = 0
    for i in f.read():
        if i in vowels:
            vowels_counter += 1
        elif i.isdigit() == True:
            number_counter += 1
        else:
            consostants_counter += 1
with open("file.txt", "r", encoding="utf-8") as f:
    lines = len(f.readlines())
with open("file.txt", "r", encoding="utf-8") as f:
    symbols = len(f.read())

with open("newfile.txt","w",encoding="utf-8") as f:
    f.write(f"Amount of symbols: {symbols}\n"
            f"Amount of lines: {lines}\n"
            f"Amount of vowels: {vowels_counter}\n"
            f"Amount of consostants: {consostants_counter}\n"
            f"Amount of numbers: {number_counter}")
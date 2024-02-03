stars = "************"

with open("../step/file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open("../step/file.txt", "w", encoding="utf-8") as f:
    for line in lines[::-1]:
        if ',' not in line:
            lines.insert((lines.index(line)) + 1, stars)
#не знаю, як зробити це
    for line in lines:
        f.writelines(line)


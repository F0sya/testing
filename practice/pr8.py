list = ["a","b","c"]
with open("../step/file.txt", "w", encoding="utf-8") as f:
    for i in list[::-1]:
        f.write(i + "\n")
list = ["a","b","c"]
with open("../step/file.txt", "w", encoding="utf-8") as f:
    for i in list:
        f.write(i + "\n")
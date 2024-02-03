with open("../step/file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open("../step/newfile.txt", "a", encoding="utf-8") as f:
    for line in lines:
        for i in line:
            if i == "*":
                f.write(i.replace("*","&"))
            elif i == "&":
                f.write(i.replace("&","*"))
            else:
                f.write(i)

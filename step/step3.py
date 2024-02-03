with open("file.txt","r",encoding="utf-8") as f:
    lines = f.readlines()[0:-1]
with open("newfile.txt","w",encoding="utf-8") as f:
    for line in lines:
        f.writelines(line)
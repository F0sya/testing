with open("../step/file.txt", 'r', encoding="utf-8") as f:
    lines = f.readlines()
with open("new_file.txt",'w',encoding="utf-8") as f:
    for line in lines[::-1]:
        f.writelines(line)
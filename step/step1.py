with open("file.txt",'r',encoding="utf-8") as f:
    data1 = set(f.readlines())
with open("newfile.txt",'r',encoding="utf-8") as f:
    data2 = set(f.readlines())
result = set(data1.difference(data2))
if result == set():
    print("No difference")
else:
    print(result)

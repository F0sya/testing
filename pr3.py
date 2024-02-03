string = "1a23&456e78uu9"
list =[]
for i in string:
    if i.isdigit():
        list.append(i)
list = [int(x) for x in list]
print(sum(list))

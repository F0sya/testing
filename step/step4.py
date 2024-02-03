with open("file.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
    longest_string = sorted(lines, key=len, reverse=True)[0]
    print(len(longest_string))
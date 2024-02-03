with open("file.txt","r",encoding="utf-8") as f:
    data = f.read()
    user_input = input("Enter a word:")
    print(data.count(user_input))
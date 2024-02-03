with open("file.txt","r",encoding="utf-8") as f:
    data = f.read()
    print(data)
user_input = input("Enter a word you want to change:")
word = input("Enter a word you want to get:")
data = data.replace(user_input,word)
with open("file.txt","w",encoding="utf-8") as f:
    f.write(data)

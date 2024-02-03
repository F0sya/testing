user_input = input("Enter a symbol:")
counter = 0
with open("../step/file.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    if line.startswith(user_input):
        counter += 1
print(counter)
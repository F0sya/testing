import os
with open("Register_file.txt", "r", encoding="utf-8") as f:
    data = f.readlines()
    logins = data[0][0:-1].split(',')
    print(logins)
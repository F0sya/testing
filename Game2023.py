a = input("a:")
b = int(input("b:"))
first_last_char = int(a[-1])
if first_last_char == 9:
    b *= 2
    first_last_char = 3
elif first_last_char == 8:
    b *= 3
    first_last_char = 2
elif first_last_char == 4:
    b*= 2
    first_last_char = 2
reshta = b % 4
if reshta != 0:
    print(int(str(first_last_char**reshta)[-1]))
else:
    print(int(str(first_last_char**b)[-1]))

#Для 0: 0
#Для 1: 1
#Для 2: 2,4,8,6
#Для 3: 3,9,7,1
#Для 4: 4,6
#Для 5: 5
#Для 6: 6
#Для 7: 7,9,3,1
#Для 8: 8,4,2,6
#Для 9: 9,1
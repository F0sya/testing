# Я вирішив зробити універсальну програму для такого типу задач, як 1 і 2 із дз, тому ось.
# Вона навіть передбачає, що юзер буде тупити і для нього є інструкція, яка викликається за бажанням
# Мені просто трохи ліньки робити кожен раз новий код для кожної задачі такого типу.
from time import sleep
list = []
n = int(input("How much numbers?"))
check = 0
for i in range(n):
    b = int(input())
    list.append(b)
list_length = len(list)
sum_number = 0
multiply_number = 1
average_number = 0
list_pos = []
subtract = 0

while check != "Yes":
    check = input("Are you familiar with the list of actions?")
    if check == "Yes":
        action = input("Which action do you want to choose?")
        if action == "max_number":
            print("Result:", max(list))
        elif action == "min_number":
            print("Result:", min(list))
        elif action == "sum_number":
            for i in range(list_length):
                sum_number = sum_number + list[i]
            print(sum_number)
        elif action == "multiply_number":
            for i in range(list_length):
                multiply_number = multiply_number * list[i]
            print(multiply_number)
        elif action == "average_number":
            for i in range(list_length):
                sum_number = sum_number + list[i]
                average_number = sum_number/n
            print(n)
        elif action == "subtract":
            for i in range(2):
                numbers_pos = int(input("Enter positions of 2 numbers you want subtract: "))
                list_pos.append(numbers_pos)
            subtract = list[list_pos[0]] - list[list_pos[1]]
            print(list[list_pos[0]], "-", list[list_pos[1]], "=", subtract)
        elif action == "divide":
            for i in range(2):
                numbers_pos = int(input("Enter positions of 2 numbers you want divide: "))
                list_pos.append(numbers_pos)
            divide = list[list_pos[0]] / list[list_pos[1]]
            print(list[list_pos[0]], "/", list[list_pos[1]], "=", divide)
    elif check == "No":
        print("List of actions: max_number, min_number, sum_number, multiply_number,average_number, subtract, divide")
        sleep(5)
    else:
        print("Error")
        sleep(5)

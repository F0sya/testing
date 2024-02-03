#Вибачте, але я взяв код з stack overflow і ваш код і трохи їх "модифікував", Також зробив систему повторної спроби вводу даних при помилці
from time import sleep
while True:
    number = input("Enter your 6 digit number:")
    result = map(int,list(number))
    result_list = list(result)

    k = -1
    if len(result_list) == 6:
        for i in range(2):
             result_list[k], result_list[i] = result_list[i], result_list[k]
             k -= 1
        print(result_list)
        break
    else:
        print("Error.\nYour number is not 6 digit.\nTry again in 3 seconds")
        sleep(3)


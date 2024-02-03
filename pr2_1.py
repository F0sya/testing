from time import sleep
while True:
    number = input("Enter your 6 digit number:")
    result = map(int, list(number))
    result_list = list(result)

    sum_1=sum(result_list[0:len(result_list)//2])
    sum_2=sum(result_list[len(result_list)//2:6])
    if len(result_list) == 6:
        if sum_1 == sum_2:
            print("Lucky Ticket")
        else:
            print("Unlucky ticket")
        break
    else:
        print("Error.\nYour number is not 6 digit.\nTry again in 3 seconds")
        sleep(3)




import random
a = random.sample(range(0,20),5)
length = len(a)
step = length // 2
number_of_action = 0
print("Default list:",a)
while step >0:
    for i in range(step, length):
        temp = i
        delta = temp - step
        while delta >= 0 and a[delta] > a[temp]:
            a[delta],a[temp] = a[temp], a[delta]
            temp = delta
            delta = temp - step
            number_of_action += 1
            print(number_of_action,"action:", a)
    step //= 2


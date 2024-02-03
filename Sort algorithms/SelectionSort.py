import random

a = random.sample(range(0,20),10)
print(a)
length = len(a)

for k in range(len(a)):
    min = k
    for j in range(k + 1,len(a)):
        if a[min] > a[j]:
            min = j
    if min != k:
        a[k],a[min] = a[min], a[k]
    print(a)


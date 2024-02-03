import random


def merge(a):
    if len(a) > 1:
        mid = len(a) // 2
        sub_arr1 = a[:mid]
        sub_arr2 = a[mid:]
        merge(sub_arr1)
        merge(sub_arr2)

        i = j = k = 0
        while i < len(sub_arr1) and j < len(sub_arr2):
            if sub_arr1[i] < sub_arr2[j]:
                a[k] = sub_arr1[i]
                i += 1
            else:
                a[k] = sub_arr2[j]
                j += 1
            k += 1

        while i < len(sub_arr1):
            a[k] = sub_arr1[i]
            i += 1
            k += 1
        while j < len(sub_arr2):
            a[k] = sub_arr2[j]
            j += 1
            k += 1
a = random.sample(range(0, 20), 10)
print(a)
merge(a)
print(a)

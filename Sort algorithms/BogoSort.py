import random


# Sorts array a[0..n-1] using Bogo sort
def bogoSort(a,tries,b):
    n = len(a)
    while not sorted(a) == b:
        if a[0] == min(a):
            b.append(a[0])
            a.remove(a[0])
        random.shuffle(a)
        tries += 1
        print(f"Sorted  B array:{b}",tries)
        print(f"A array:{a}")


# Driver code to test above
a = random.sample(range(0, 100),100)
b = []
tries = 0
bogoSort(a,tries,b)
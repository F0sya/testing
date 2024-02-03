from colorama import Fore
a = [int(x) for x in open("../list.txt", 'r').read().splitlines()]
n = len(a)
L = 0
R = n - 1
number_of_action = 0
print(f"Default list{a}")
while L != R:
    for i in range(R,L-1,-1):
        if i == L:
            L += 1
            break
        elif a[i] < a[i-1]:
            a[i], a[i-1] = a[i-1], a[i]
            number_of_action += 1
            print(Fore.RED +f"{number_of_action} action: {a}")
    for k in range(L-1,R+1):
        if k == R:
            R -= 1
            break
        elif a[k] > a[k+1]:
            a[k],a[k+1] = a[k+1],a[k]
            number_of_action += 1
            print(Fore.RED + f"{number_of_action} action: {a}")

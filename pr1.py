sentence = input("Введіть речення:")
vowels = {'a','e','i','o','u','y'}
for i in sentence:
    if i in vowels:
        vowels -= set(i)
        print(i)




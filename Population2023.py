input = input()
list = [int(x) for x in input.split()]
N = list[0]
list.pop(0)
i = 0
result = max(list)
list.remove(result)
sum = sum(list)
list.append(result)
if sum > result:
    sum,result = result, sum
n = result - sum
print(result - n)
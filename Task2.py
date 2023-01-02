#Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

num = int(input())
sum = 0
if num > 0:
    for i in range(1, num + 1):
        sum += i
elif num < 0:
    for i in range(1, num - 1, -1):
        sum += i
elif num == 0:
    sum = 1
print(sum)
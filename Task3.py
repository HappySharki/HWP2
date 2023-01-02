#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n = int(input())
i = 1

for i in range(2, n + 1):
    if not n % i:
        print(i)
        break
#Петя впервые пришел на урок физкультуры в новой школе. 
#Перед началом урока ученики выстраиваются по росту, в порядке невозрастания. 
#Напишите программу, которая определит на какое место в шеренге Пете нужно встать, 
#чтобы не нарушить традицию, если заранее известен рост каждого ученика и эти данные 
#уже расположены по невозрастанию (то есть каждое следующее число не больше предыдущего). 
#Если в классе есть несколько учеников с таким же ростом, как у Пети, то программа должна расположить его после них.

num = int(input("Количество учеников: "))
list_of_heigth = []
for i in range(num):
    heigth = int(input(f"Рост {i + 1} ученика: "))
    list_of_heigth.append(heigth)
petya = int(input("Рост Пети: "))
list_of_heigth.append(petya)
list_of_heigth.sort(reverse=True)
print(list_of_heigth.index(petya) + 1)


lst = []
for i in range(int(input("Кол-во: "))):
    lst.append(int(input("Рост по убыванию: ")))
pet = int(input("Рост Пети: "))
for j in range(len(lst)):
    if lst[j] <= pet:
        print(j + 1)
        break

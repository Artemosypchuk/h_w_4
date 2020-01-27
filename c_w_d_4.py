
# # file = open("list.txt",'w')
# # file.write(str(arr2))
# # file.close()

import random
import colorama
from colorama import Fore, Back, Style
colorama.init()
"""
1 Дано список. Знайти найбільший та найменший елементи масиву та поміняти їх у      масиві місцями.
2 Дано список. Дано одновимірний масив. Знайти найбільший та найменший елементи     масиву та поміняти їх у масиві місцями.
3 Дано список. Поміняти місцями перший елемент з другим, третій з четвертим, і      т.д. Вивести змінений масив на екран
4 Дано список(А) із К елементів (К- парне число). Утворити 2 списки(В і С),         переписуючи у списку В першу половину масиву А, у список С – другу половину         масиву А

"""
print(Fore.YELLOW+"Hello This is my home work")
input("'Enter' для продовження...")
task_1 = print(Fore.GREEN +
               "\t\t\tЗадача № 1\n1 Дано список. Знайти найбільший та найменший елементи масиву та поміняти їх у      масиві місцями.")
input("'Enter' для продовження...")
print("Створюємо список за допомогою модулю 'random' ")
input("'Enter' для продовження...")
arr = []

for a in range(0, 21):  # список з 20 елементів
    # заповнюємо список випадковими числами від 0 - 99
    arr.append(random.randint(0, 99))
arr.sort()  # сортуємо список
print(Fore.GREEN+"Відсортирований список: ", arr)
min_value = min(arr)  # знаходимо найменьше значення
max_value = max(arr)  # знаходимо найбільше значення
min_index = arr.index(min_value)  # знаходимо індекс найменьшого значення
max_index = arr.index(max_value)  # знаходимо індекс найбільшого значення
z = arr[max_index]  # створюємо змінну із максимальним значенням
arr[max_index] = arr[min_index]  # міняємо значення місцями
arr[min_index] = z  # міняємо значення місцями
print(Fore.BLUE+"Новий масив з поміняними найбільшим та найменьшим значеннями: ", arr)
print(Fore.YELLOW+"Перша задача зроблена"+Fore.RESET)
input("'Enter' для продовження...")

while True:
    next = input(
        'Оберіть дію, введіть:\n "n" - для продовження\n"w" - для запису в файл: ')
    if next == 'n':
        print("Ви не зберегли дані!")
        break
    elif next == 'w':
        file = open("Home_Work.txt", 'w', encoding='UTF-8')
        task_1 = "Задача № 1\n"
        file.write(task_1)
        file.write(str(arr))
        txt = "\nСписок відсортовано..."
        file.write(txt)
        file.close()
        file = open("Home_Work.txt", 'r', encoding='UTF-8')
        f = file.read()
        print(f)
        file.close
        print(Fore.CYAN+"Файл успішно збережено!"+Fore.RESET)
        break


print(Fore.GREEN+"\t\t\tЗадача № 2\n3 Дано список. Поміняти місцями перший елемент з другим, третій з четвертим, і      т.д. Вивести змінений масив на екран.")
input("'Enter' для продовження...")


arr2 = []
for a in range(0, 22):  # список з 21 елементу
    # заповнюємо список випадковими числами від 0 - 99
    arr2.append(random.randint(0, 99))
arr2.sort()  # сортуємо список

x = 0
print(Fore.BLUE+"старий масив: ", arr2)

for i in range(0, len(arr2)//2):
    arr2[x], arr2[x+1] = arr2[x+1], arr2[x]
    x = x + 2

print(Fore.YELLOW+"відсортирований масив: ", arr2)
input("'Enter' для продовження...")
while True:
    next = input(
        'Оберіть дію, введіть:\n "n" - для продовження\n"w" - для запису в файл: ')
    if next == 'n':
        print("Ви не зберегли дані!")
        break
    elif next == 'w':
        file = open("Home_Work.txt", 'a', encoding='UTF-8')
        task_1 = "\nЗадача № 2\n"
        file.write(task_1)
        file.write(str(arr2))
        txt = "\nСписок відсортовано..."
        file.write(txt)
        file.close()
        file = open("Home_Work.txt", 'r', encoding='UTF-8')
        f = file.read()
        print(f)
        file.close
        print(Fore.CYAN+"Файл успішно збережено!"+Fore.RESET)
        break

print(Fore.GREEN+"\t\t\t Задача №3\nДано список(А) із К елементів (К- парне число). Утворити 2 списки(В і С), переписуючи у списку В першу половину масиву А, у список С – другу половину масиву А")
input("'Enter' для продовження...")
list_a = []
for a in range(0, 20):  # список з 20 елементів
    # заповнюємо список випадковими числами від 0 - 99
    list_a.append(random.randint(0, 99))
list_a.sort()  # сортуємо список
print(Fore.YELLOW+"Даний список 'А': ", list_a)
list_b = []
list_c = []
for z in range(len(list_a)):
    if z < len(list_a)/2:
        list_b.append(list_a[z])
    else:
        list_c.append(list_a[z])

print(Fore.BLUE+"Перша полловина списку 'B': ", list_b)
print(Fore.GREEN+"Друга полловина списку 'C': ", list_c)
while True:
    next = input(
        'Оберіть дію, введіть:\n "n" - для продовження\n"w" - для запису в файл: ')
    if next == 'n':
        print("Ви не зберегли дані!")
        break
    elif next == 'w':
        file = open("Home_Work.txt", 'a', encoding='UTF-8')
        task_1 = "\nЗадача № 3\n"
        file.write(task_1)
        file.write(str(list_a))
        file.write("\n")
        file.write(str(list_b))
        file.write("\n")
        file.write(str(list_c))
        txt = "\nСписок відсортовано..."
        file.write(txt)
        file.close()
        file = open("Home_Work.txt", 'r', encoding='UTF-8')
        f = file.read()
        print(f)
        file.close
        print(Fore.CYAN+"Файл успішно збережено!"+Fore.RESET)
        break
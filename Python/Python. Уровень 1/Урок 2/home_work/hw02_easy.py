# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

'''
fruit_list = ["яблоко", "банан", "киви", "арбуз", "апельсин", "виноград", ]
count = 0
num = 1

while count < len(fruit_list):
    print('{}. {}'.format(num, fruit_list[count]))
    num += 1
    count += 1
'''

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


import random

# Собираем произвольный список
def random_list():
    num_list = []
    count = 0
    while count < 10:
        num = int(random.randrange(10, 20))
        num_list.insert(count, num)
        count += 1

    return num_list

num_list_1 = random_list()
num_list_2 = random_list()
count = 0

print('Произвольный список 1:', num_list_1)
print('Произвольный список 2:', num_list_2)

while count < len(random_list()):
    if num_list_1[count] == num_list_2[count]:
        del num_list_1[count]

print('Новый список 1:', num_list_1)

#while count > len(random_list()):
#    if int(num_list_1[count]) == 11:
 #       del num_list_1[count]

#    count += 1

#print(num_list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

'''
import random

num_list = []
new_num_list = []
count = 0
new_count = 0

# Собираем произвольный список
while count < 10:
    num = int(random.randrange(10, 100))
    num_list.insert(count, num)
    count += 1

print('Произвольный список:', num_list)

# Собираем новый список согласно условиям задачи
while new_count < len(num_list):
    if num_list[new_count]%2 == 0:
        result = num_list[new_count]/4
        new_num_list.insert(new_count, result)
    else:
        result = num_list[new_count] * 2
        new_num_list.insert(new_count, result)
    new_count += 1

print('Новый список: {}'.format(new_num_list))
'''





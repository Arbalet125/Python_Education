# Вычислить число c заданной точностью d. 
# (Насколько я понимаю, в этой задаче нужно задать округленное число знаков после запятой числа ПИ. Если это так, то решение следующае:)

# from math import pi

# d =  int(input("Введите число для заданной точности числа Пи: "))
# rigour = round(pi, d)
# print()
# print(f"Число ПИ с заданной точностью {d}, равно:\n", rigour)

###################################################################################

#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

# number = int(input("Введите число натуральное число N: "))
# i = 2
# lst = []
# fake_number = number
# while i <= number:
#     if number % i == 0:
#         lst.append(i)
#         number //= i
#     else:
#         i += 1
# print()
# print(f"Простые множители числа {fake_number} равняются:\n", str(lst).strip('[').strip(']'))

###################################################################################

#Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = list(map(int, input("Введите целые числа чтобы заполнить список (в качестве разделителя между числами используйте пробел):\n").split()))
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов списка \n", lst, "\nРавен следующему списку: \n", new_lst)

###################################################################################

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k. 

# import random

# def write_file(st):
#     with open('file_dz_seminar4.txt', 'w') as data:
#         data.write(st)


# def rnd():
#     return random.randint(0,101)


# def create_spisok_koeficent(k):
#     lst = [rnd() for i in range(k+1)]
#     return lst
    

# def create_str(sp):
#     lst= sp[::-1]
#     wr = ''
#     if len(lst) < 1:
#         wr = 'x = 0'
#     else:
#         for i in range(len(lst)):
#             if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                 wr += f'{lst[i]}x^{len(lst)-i-1}'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 2 and lst[i] != 0:
#                 wr += f'{lst[i]}x'
#                 if lst[i+1] != 0:
#                     wr += ' + '
#             elif i == len(lst) - 1 and lst[i] != 0:
#                 wr += f'{lst[i]} = 0'
#             elif i == len(lst) - 1 and lst[i] == 0:
#                 wr += ' = 0'
#     return wr

# k = int(input("Введите натуральную степень k = "))
# spisok_koeficent = create_spisok_koeficent(k)
# write_file(create_str(spisok_koeficent))
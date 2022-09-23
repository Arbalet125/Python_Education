# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# my_list = [1, 3, 2, 4, 3, 5, -2]
# print(max(my_list), min(my_list))

# Преподское решение:
# some_str = input() # '1 2 3 4 5'
# some_list = some_str.split() # ['1', '2', '3', '4', '5']
# some_int_list = list(map(int, some_list)) # [1, 2, 3, 4, 5]
# print(max(some_int_list), min(some_int_list))

# Преподское решение #2:
# some_str = input() # '1 2 3 4 5'
# print(max(list(map(int, some_str.split()))), min(list(map(int, some_str.split()))))

##########

# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1. с помощью математических формул нахождения корней квадратного уравнения
# 2. с помощью дополнительных библиотек Python

# import math 

# def findRoots(a, b, c): 
 
#     dis_form = b * b - 4 * a * c 
#     sqrt_val = math.sqrt(abs(dis_form)) 
 
 
#     if dis_form > 0: 
#         print(" real and different roots ") 
#         print((-b + sqrt_val) /(2 * a)) 
#         print((-b - sqrt_val) /(2 * a)) 
 
#     elif dis_form == 0: 
#         print(" real and same roots") 
#         print(-b /(2 * a)) 
 
 
#     else: 
#         print("Complex Roots") 
#         print(- b /(2 * a), " + i", sqrt_val) 
#         print(- b /(2 * a), " - i", sqrt_val) 
 
 
# a = int(input('Enter a:')) 
# b = int(input('Enter b:')) 
# c = int(input('Enter c:')) 
 
# # If a is 0, then incorrect equation 
# if a == 0: 
#     print("Input correct quadratic equation") 
 
# else: 
#     findRoots(a, b, c) 

# Преподское решение:

# import sympy as sm
#
# x = sm.Symbol('x')
# a = int(input())
# b = int(input())
# c = int(input())
# print(sm.solveset(a * x ** 2 + b * x + c, x))


##########

# Задайте два целых числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# x, y = 4, 6
# if x > y: big_num = x
# else: big_num = y
# while(True):
#     if (big_num % x == 0) and (big_num % y == 0):
#         result = big_num
#         break
#     big_num += 1
# print(result)

# Преподское решение:

# import sympy as sm
# a = int(input())
# b = int(input())
# print(sm.lcm(a, b))
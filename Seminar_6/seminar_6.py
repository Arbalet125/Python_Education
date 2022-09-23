# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 


number_1 = input("Введите первое число: ")
print("Выберите действие: ")
operator = (input("(сложение (+), вычитание (-), умножение (*), деление (/)"))
number_2 = input("Введите второе число: ")
print(f"Pезультат:", eval(number_1 + operator + number_2))

# Преподское решение:




###########################

# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# from random import randint

# def create_list(size, m, n):
#     return [randint(m, n) for i in range(size)]

# def get_unic_value(list):
#     return [i for i in set(list)]

# size = 10
# m = 1
# n = 10

# origin = create_list(size, m, n)
# print(origin)
# print(get_unic_value(origin))

####

my_list = [1, 2, 3, 5, 1, 5, 3, 10]

# res = list(filter(lambda x: my_list.count(x)==1, my_list))
res = [x for x in my_list if my_list.count(x)==1]

print(res)

# Преподское решение:


###########################
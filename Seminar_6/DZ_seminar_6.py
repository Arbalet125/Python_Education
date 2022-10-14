# Задание №1:
# Представлен список чисел. Необходимо вывести элементы исходного списка, значения
# которых больше предыдущего элемента.

# import random
# leng = int(input("Введите количество чисел в списке: "))

# my_list = [random.randint(0, 100) for i in range(leng)]

# res = []
# for i in range(1, len(my_list)):
#     if my_list[i] > my_list[i-1]:
#         (res.append(my_list[i]))

# # [res.append(my_list[i]) for i in my_list if my_list[i] > my_list[i-1]]


# print("Исходный список: ", my_list)
# print("Список, элементы которого больше предыдущего: ", res)

########################################################

# Задание №2:
# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21.

# n_number = int(input("Введите число N: "))

# my_list = [i for i in range(20, n_number) if i % 20 == 0 or i % 21 == 0]
# print(my_list)

########################################################

# Задание №3: 
# Написать функцию аргументы имена сотрудников,возвращает словарь, 
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. 

# def colleagues(*args):
#     colleagues_dict = {}
#     for i in args:
#         if i[0] in colleagues_dict.keys():
#             colleagues_dict[i[0]].append(i)
#         else:
#             colleagues_dict[i[0]] = [i]
#     print(colleagues_dict)

    
# colleagues("Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка")


########################################################

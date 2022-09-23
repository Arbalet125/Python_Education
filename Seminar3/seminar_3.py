# Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

# from time import time
# print(f'Случайное число от 0 до 99 = {int(time() % 1 * 100)}')

# Преподское решение:

# import time
# now = time.time()
# print(int(str(now).split('.')[1]) % 100) #[1] относится к правой части числа, что после точки. Если нужна правая, выбираем [0]

###################

# Задача №20: Определить, присутствует ли в заданном списке строк, некоторое число

# lst_len = int(input("Введите количество строк для создания списка: "))
# lst = [input(f"Введие {i+1} строку: ") for i in range(lst_len)]
# number = input("Введите число для поиска: ")
# flag = False
# for i in lst:
#     if number in i:
#         flag = True
#         break
# print("Присутствует" if flag else "Не присутствует")

# # Преподское решение:

# some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
# el = input('Введите искомое число: ')
# for i in some_list:
#     if el in i:
#         print('YES')
#         break
# else:
#     print('NO')

###################

# Задача №21: Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1


# def my_func(lst, find_str):
#     if lst.count(find_str) > 1:
#         k = lst.index(find_str)
#         print(lst.index(find_str, k+len(find_str)))
#     else:
#         print(-1)

# lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# f = "qwe"
# my_func(lst, f)
# lst = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# f = "йцу"
# my_func(lst, f)
# lst = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# f = "йцу"
# my_func(lst, f)
# lst = ["123", "234", 123, "567"]
# f = "123"
# my_func(lst, f)
# lst = []
# f = "123"
# my_func(lst, f)

# Преподское решение:

# some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
# el = input('Введите искомую строку: ')
# c = 0
# if some_list.count(el) != 2:
#     print(-1)
# else:
#     for i in range(len(some_list)):
#         if some_list[i] == el:
#             c += 1
#     if c == 2:
#         print(i)
#         break

# Преподское решение №2:

# some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
# el = input('Введите искомую строку: ')
# first = some_list.index(el)       # команда index ищет все элементы в скобках () в списке some_list
# second = some_list.index(el, first + 1)
# print(second)
# Эта конструкция не работает, если у нас получается отрицательный ответ (элоементы не входят друг в друга), чтобы работало, юзаем:

# Преподское решение №3:

# some_list = [input('Введите строку: ') for _ in range(int(input('Введите кол-во элементов: ')))]
# el = input('Введите искомую строку: ')
# try:
#     print(some_list.index(el, some_list.index(el) + 1))
# except:
#     print(-1)
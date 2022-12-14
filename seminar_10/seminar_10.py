# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном
# списке, например:
# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.

# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

# ls = [i for i in src if src.count == 1]
# print(ls)

# Оптимизация:

# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# a = set() #23 1 3 10 4 11
# b = set() #2 7 23 1 44 3 10 4 11
# for i in src:
#     if i not in b:
#         a.add(i)
#     else:
#         a.discard(i)
#     b.add(i)
# print(list(a))

####################################################

# Напишите программу, которая удаляет из строки все повторяющиеся символы.
# На вход программы подается строка, содержащая символы ASCII
# Программа должна вывести исходную строку, их которой удалены все повторяющиеся символы


# s = input()
# s_final = ''
# set_s = list(set(s))
# s_final = ''.join(set_s)

# print(s_final)

####################################################

# Напишите программу, которая находит все цифры, которых нет в переданной ей строке.
# На вход программы подается символьная строка.
# Программа должна вывести в одной строке все цифры, в которые не встречаются в исходной строке, в порядке убывания.
# Если таких цифр нет, программа должна вывести "No"


# s_digit = "9876543210"
# s = input()
# digit_set = set()
# for i in s:
#     if i.isdigit():
#         digit_set.add(i)

# s_final = ""
# for i in s_digit:
#     if i in digit_set:
#         s_final += i

# if s_final :
#     print(s_final)
# else:
#     print("No")

# В одну строку:

# s = input()
# res = ''.join(str(i) for i in range(10)[::-1] if str(i) not in s)
# print(res if res else 'NO')

####################################################
# Напишите программу, которая находит все символы, встречающиеся в обеих переданных ей строках.
# На вход программы подаются две символьные строки.
# Программа должна вывести все символы, которые встречаются в обеих строках, в порядке возрастания ASCII-кодов,
# если таких символов нет, нужно вывести слово "No" 

# s1 = input()
# s2 = input()

# set_1 = set(s1)
# set_2 = set(s2)

# print(set_1.intersection(set_2))

####################################################


# Напишите программу, которая вводит две символьные строки и находит все латинские буквы, 
# которых нет ни в одной из них. Заглавные и строчные буквы не различаются.
# Входные данные
# На вход программе подаются две символьные строки.
# Выходные данные
# Программа должна вывести в одной строке в алфавитном порядке все латинские буквы, 
# которые не встречаются ни в одной из двух входных строк. Все буквы должны быть заглавными. 
# Если ни одной такой буквы нет, нужно вывести число 0.

# from string import ascii_letters
#
# s_letters = set(list(i for i in ascii_letters if i.upper() != i))
#
# s1 = input()
# s2 = input()
# set_1 = set(s1)
# set_2 = set(s2)
#
# s_final = ''.join(sorted(list(i.upper() for i in (''.join(list(s_letters.difference(set_1.union(set_2))))))))
#
# if s_final:
#   print(s_final)
# else:
#   print(0)
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = input("Введите число цифры которого необходимо сложить: ")
# fakeN = n # если вдруг в конце понадобиться изначальное число N (например для вывода в конце)
# str_n = str(n) # переводим введенные цифры в строку
# str_n = str_n.replace('.', '') # заменяем все возможные точки (если пользователь ввел вещественное число с точкой) на пробелы, для того, чтобы можно было использовать функцию sum к строке в дальнейшем
# str_n = str_n.replace(',', '') # то же самое, только с запятыми (если пользователь ввел вещественное число и разделителем выбрал запятую)
# lst_str = list(str_n) # загоняем строчку в массив
# lst_num = map(int, lst_str) #преобразуем строчку в массиве в числа

# summa = sum(lst_num) #используем функцию, чтобы просуммировать все цифры массива
 

# print(f"Сумма цифр числа {fakeN} равна:", summa)

###################################################################################

#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input("Введите число N: "))
# fakeN = n
# factList = [1]
# factorial = 1
# while n > 1:
#     factorial *= n
#     factList.append(factorial)
#     n -= 1
# print (f"Пусть N = {fakeN}, тогда: ", factList)

###################################################################################

#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input("Введите количество чисел в последовательности: "))
# some_dict = {}
# some_list = []
# for i in range(1, n + 1):
#     some_dict[i] = round((1+(1/i))**i, 2) #округлил для красоты вывода
#     some_list.append((1+(1/i))**i)
# summa = sum(some_list)
# print(f"Cумма чисел последовательности: ", some_dict, "равняется:", summa)

#Реализуйте алгоритм перемешивания списка

# sample_list = [1, 2, 3, 4]
# print("Исходный список: ")
# print(sample_list)
# import random
# # random.shuffle(sample_list)
# print("Перемешанный список: ")
# print(sample_list)    #на семинаре, вроде бы, сказали, что этого будет достаточно

# но если нет:

# import random
# sample_list = [1, 2, 3, 4]
# second_list = sample_list[:]
# list_length = len(sample_list)
# for i in range(list_length):
#     index_temp = random.randint(0, list_length - 1)
#     temp = sample_list[i]
#     second_list[i] = sample_list[index_temp]
#     second_list[index_temp] = temp
# print("Исходный список: ")
# print(sample_list)
# print("Перемешанный список: ")
# print(second_list)
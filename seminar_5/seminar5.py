# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 5

# num = ''

# def fun(num):
#     for i in range(0,len(num)):
#         if (num[i+1])-num[i] != 1:
#             return num[i]+1


# with open('numfile.txt', 'r') as data:
    
#     num = data.read()

# num = list(map(int,num.split(', ')))

# print(fun(num))

####################################################

# Дан список чисел. Создать список, в который попадают числа,
# описываемые возрастающую последовательность.
# *Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.*
# ***Порядок элементов менять нельзя***

# nums = [3, 1, 2, 3, 4, 6, 1, 7]

# # Первый вариант

# def get_up2(nums):
#     ups = [nums[0]]
#     for i in nums:
#         if i > max(ups):
#             ups.append(i)
#     return ups
    
# print(get_up2(nums))

# # Второй вариант

# def get_up(nums):
#     ups = []
#     for i in range(len(nums)):
#         if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
#             ups.append(nums[i])
#     return ups

# print(get_up(nums))

# Заловое решение

# num = [1, 5, 2, 3, 4, 6, 1, 7]

# def nextmax(listt):    
#     max = listt[0]
#     res = [listt[0]]
#     for i in range(len(listt)):
#         if listt[i] > max:
#             max = listt[i]
#             res.append(max)
        
#     return res

# print(nextmax(num))

# Заловое решение

# list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = [list[0]]
# max = list[0]
# for i in list:
#     if i > max:
#         new_list.append(i)
#         max = i
# print(new_list)

# Преподское решение

# my_list = [1, 5, 2, 3, 4, 6, 1, 7]

# res = [my_list[0]]
# [res.append(item) for item in my_list if item > res[-1]]
# print(res)


########################################################

# 38. Напишите программу, удаляющую из 
# текста все слова содержащие "абв".

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_words(my_text)
# print(my_text)

# Заловое решение

# print (' '.join(filter(lambda x: not 'абв' in x,'Мы неабв очень любим Питон иабв Джавуабв!'.split())))


# Дискорд: https://discord.gg/cJvrFc2w
# Телеграм: @slavalk


# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 2. Создайте программу для игры с конфетами человек против человека.
    
#     Условие задачи: На столе лежит 2021 конфета. 
#     Играют два игрока делая ход друг после друга. 
#     Первый ход определяется жеребьёвкой. 
#     За один ход можно забрать не более чем 28 конфет. 
#     Все конфеты оппонента достаются сделавшему последний ход. 
    
#     a) Добавьте игру против бота
    
#     b) Подумайте как наделить бота "интеллектом"
#     (Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?)
    
# 3. Создайте программу для игры в "Крестики-нолики".

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaffffcc
# a3f4c2
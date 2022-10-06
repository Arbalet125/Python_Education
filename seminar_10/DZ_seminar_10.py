# Задача №1: Даны два списка чисел. Найдите все числа, которые входят как в первый, 
# так и во второй список и выведите их в порядке возрастания.
# В одну строку

# my_list = sorted(list(set([int(s) for s in input().split()]) & set([int(s) for s in input().split()])))
# for i in my_list:
#     print(i, end=' ')

################################################

# Задача №2 
# Во входной строке записана последовательность чисел через пробел. 
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности 
# или NO, если не встречалось.

# numbers = [int(i) for i in input().split()]
# set_numbers = set()
# for i in numbers:
#     if i in set_numbers:
#         print('YES')
#     else:
#         print('NO')
#     set_numbers.add(i)

################################################

# Задача №3 
# Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов
# содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд, слова разделены одним 
# или большим числом пробелов или символами конца строки.


# sample_str = '''4                                                     # это число тоже будет считаться строкой и словом
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.'''

# print(sample_str)

# set_str = set()

# for i in sample_str:
#     S = sample_str.split()
#     for elem in S:
#         set_str.add(elem)
# print(len(set_str))
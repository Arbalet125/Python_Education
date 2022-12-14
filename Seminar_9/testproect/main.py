# some_dict = {'name': 'Ivan', # первый параметр (в данном случае: "name") - ключ, второй - значение
#              'last_name': 'Ivanov',
#              'age': 32
#             }

# print(some_dict["age"])
# print(some_dict.get('sdsdsfdf', "Key not found"))
# print(some_dict.setdefault("adress", "Berezevaya 1"))
# print(some_dict)

#####################

# Есть два списка, сформировать словарь так, чтобы элементы первого списка были ключами для второго

# first_list = [1, 2, 3, 4, 5]
# second_list = ['a', 'b', 'c', 'd', 'e']
# some_dict = {}
# for i in range (len(first_list)):
#     some_dict[first_list[i]] = second_list[i]
# print(some_dict)

#######################################

# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. 
# Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

# ДОПОЛНЕНИЕ: Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

# Мое решение:

# my_dict = {"one": "один",
#            "One": "Один",
#            "two": "два",
#            "Two": "Два",
#            "three": "три",
#            "Three": "Три",
#            "four": "четыре",
#            "Four": "Четыре",
#            "five": "пять",
#            "Five": "Пять",
#            "six": "шесть",
#            "Six": "Шесть",
#            "seven": "семь",
#            "Seven": "Семь",
#            "eight": "восемь",
#            "Eight": "Восемь",
#            "nine": "девять",
#            "Nine": "Девять",
#            "ten": "десять",
#            "Ten": "Десять"
#            }

# def num_translate():
#     print(my_dict.get(input("Введите числительное для перевода: ")))

# num_translate()

################

# Преподское решение:

# def num_translate(number):
#     translate_dict = {"one": "один",
#                "two": "два",
#                "three": "три",
#                "four": "четыре",
#                "five": "пять",
#                "six": "шесть",
#                "seven": "семь", 
#                "eight": "восемь",
#                "nine": "девять",
#                "ten": "десять"
#            }
#     if number[0].isupper():
#         print(translate_dict.get(number.lower()).capitalize())
#     else:
#         print(translate_dict.get(number))


# num_translate('one')
# num_translate('One')

###############################

# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы. 
# Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
# "И": ["Иван", "Илья"],
# "М": ["Мария"], "П": ["Петр"]
# }



# def tesarius(*args):
#     tesarius_dict = {}
#     for i in args:
#         if i[0] in tesarius_dict.keys():
#             tesarius_dict[i[0]].append(i)
#         else:
#             tesarius_dict[i[0]] = [i]
#     print(tesarius_dict)
    
# tesarius("Иван", "Мария", "Петр", "Илья")



# Неверное решение:
# thesarius_dict = {"А": ["Анна", "Артем", "Артур"],
#                   "И": ["Иван", "Илья"],
#                   "М": ["Мария"],
#                   "П": ["Петр"]
#                   }

# def thesarius():
#     print(thesarius_dict.get(input("Введите первую букву фамилии: "), "Фамилия на такую букву не найдена"))

# thesarius()

###############################

#  4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки 
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, 
# реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. 
# 
# Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
# "А": {
# "П": ["Петр Алексеев"]
# },
# "И": {
# "И": ["Илья Иванов"]
# },
# "С": {
# "И": ["Иван Сергеев", "Инна Серова"],
# "А": ["Анна Савельева"]
# }
# }
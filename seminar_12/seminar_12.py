# class Auto():
#     def __init__(self, price):
#         self.price = price

#     def __add__(self, other):
#         return self.price + other.price

#     def __str__(self):
#         return "Привет, я машина"
    
#     def __gt__(self, other):
#         return self.price > other.price


# a = Auto(1000000)
# b = Auto(2000000)
# print (a+b)
# print(a)
# print (a > b)

########################################


# class Foodlnfo:
#     def __init__(self, proteins, fats, carbohydrates):
#         self.proteins = proteins
#         self.fats = fats
#         self.carbohydrates = carbohydrates
    
#     def get_proteins(self):
#         return self.proteins
    
#     def get_fats(self):
#         return self.fats
    
#     def get_carbohydrates(self):
#         return self.carbohydrates    
    
#     def get_kcalories(self):
#         return self.get_proteins()*4 + self.get_fats()*9 + self.get_carbohydrates()*4
    
#     def __add__(self, other):
#         return Foodlnfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
    
#     # def __str__(self):
#     #     return f"Объект с параметрами ({self.width}, {self.height})"

# mc_1 = Foodlnfo(10, 20, 30)
# mc_2 = Foodlnfo(30, 40, 50)
# mc_3 = mc_1 + mc_2
# print(mc_3.get_proteins(), mc_3.get_fats(), mc_3.get_carbohydrates(), mc_3.get_kcalories())


###########################

# Список в обратном порядке
# Ограничение времени	1 секунда
# Ограничение памяти	64МЬ
# Ввод	стандартный ввод или test.py
# Вывод	стандартный вывод или output.txt

# Напишите класс ReversedList, который будет при инициализации 
# экземпляра принимать список и реализовывать доступ к элементам 
# этого списка в обратном порядке.
# rl = ReversedList(lst) — создание обратного списка.
# len(rl) — число элементов в обратном списке.
# rl[i]   — доступ к элементам в обратном порядке. 
# rl[0] — последний элемент первоначального списка. 
# rl[1] — предпоследний и 
# Пример 1:
# from solution import ReversedList
# rl = ReversedList([10, 20, 30]) 
# for i in range(len(rl)): 
#     print(rl[i])

# class ReversedList:
#     def __init__(self, some_list):
#         self.some_list = list(reversed(some_list))

#     def __getitem__(self, item):
#         return self.some_list[item]

#     def __len__(self):
#         return len(self.some_list)

# rl = ReversedList([10, 20, 30])
# for i in range(len(rl)):
#     print(rl[i])

# rl = ReversedList([])
# print(len(rl))

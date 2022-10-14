#рок 6. Задание 1:
#  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
#  Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный,
#  желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
#  третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
#  порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

# import time

# class TrafficLight():

#     # Определяем время ожидания сигнала светофора
#     red_color_wait = 7
#     yellow_color_wait = 2
#     green_color_wait = 4

#     # Определяем названия цветов сигналов светофора
#     red_color_name = 'красный'
#     yellow_color_name = 'желтый'
#     green_color_name = 'зеленый'

#     def __init__(self, color):
#         self.__color = color
#         print(f'\nСоздан новый объект TrafficLight со стартовым цветом {self.__color}')

#     def switch_light(self, color, wait_period):
#         self.wait_period = wait_period
#         print(f'Включен {color} свет, время ожидания {self.wait_period} сек')
#         time.sleep(self.wait_period)

#     def running(self, color = ''):

#         # Если при вызове метода цвет не указан, берем из родительского класса
#         # В противном случае стартуем с цвета, объявленного при вызове метода
#         if not color:
#             loc_color = self.__color
#         else:
#             loc_color = color

#         if loc_color == self.red_color_name:
#             self.switch_light('красный', self.red_color_wait)
#             self.switch_light('желтый', self.yellow_color_wait)
#             self.switch_light('зеленый', self.green_color_wait)
#         elif loc_color == self.yellow_color_name:
#             self.switch_light('желтый', self.yellow_color_wait)
#             self.switch_light('зеленый', self.green_color_wait)
#         else:
#             self.switch_light('зеленый', self.green_color_wait)

#         print('Цикл переключения цветов завершен')

# tl1 = TrafficLight('красный')
# tl1.running()

# tl2 = TrafficLight('желтый')
# tl2.running()

# tl3 = TrafficLight('зеленый')
# tl3.running()

# # Инициализируем класс красным цветом, а метод запускаем с желтого
# tl1 = TrafficLight('красный')
# tl1.running('желтый')


# Задание №2:
# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


# class Road:
#     _length = 0
#     _width = 0

#     def __init__(self, _length, _width, weight, depth):
#         self._length = _length
#         self._width = _width
#         self.weight = weight
#         self.depth = depth

#     def mass(self):
#         leng = self._length
#         wid = self._width
#         w = self.weight
#         dep = self.depth
#         total = leng * wid * w * dep / 1000
#         return print(f"Масса асфальта\n {leng} м * {wid} м * {w} кг * {dep} см = ", total, "т")


# r = Road(20, 5000, 25, 5)
# r.mass()

# Напишите класс TicTacToeBoard для игры в крестики-нолики, который должен иметь следующие методы:
# * new_game() - для создания новой игры;
# * get_field() - для получения поля (список списков)
# * check_field() - для проверки есть ли победитель, который возвращает Х если победил первый
# игрок, 0 - если второй, D - если ничья и None если можно продолжать игру.
# * make_move(row, col) - который устанавливает значение текущего хода в ячейку поля с координатами
# row, col, если это возможно, переключает ход игрока, а также выдает сообщение "Победил игрок Х", при
# победе крестиков, "Победил игрок 0", при победе ноликов, "Ничья", в случае ничьей и "Продолжаем играть",
# если победитель после данного хода не определен.

# Кроме того, метод make_move должен возвращать сообщение "клетка уже занята", если в клетке стоит крестик
# или нолик.

# При создании объекта класса должна создаваться новая игра.
# Аргументы row и col могут принимать значения от 0 до 3.

# class TicTacToeBoard:
#     def __init__(self):
#         self.clear_place = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
#         self.p = self.clear_place
#         self.end_info = 0
#         self.list = ['X', '0']
#         self.n = 1
 
#     def new_game(self):
#         self.clear_place = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
#         self.p = self.clear_place
#         self.end_info = 0
#         self.list = ['X', '0']
#         self.n = 1
 
#     def get_field(self):
#         return self.p
 
#     def check_field(self):
#         if (self.p[0][0] == 'X' and
#             self.p[0][1] == 'X' and
#             self.p[0][2] == 'X') or \
#                 (self.p[1][0] == 'X' and
#                  self.p[1][1] == 'X' and
#                  self.p[1][2] == 'X') or \
#                 (self.p[2][0] == 'X' and
#                  self.p[2][1] == 'X' and
#                  self.p[2][2] == 'X') or \
#                 (self.p[0][0] == 'X' and
#                  self.p[1][1] == 'X' and
#                  self.p[2][2] == 'X') or \
#                 (self.p[0][2] == 'X' and
#                  self.p[1][1] == 'X' and
#                  self.p[2][0] == 'X') or \
#                 (self.p[0][0] == 'X' and
#                  self.p[1][0] == 'X' and
#                  self.p[2][0] == 'X') or \
#                 (self.p[0][1] == 'X' and
#                  self.p[1][1] == 'X' and
#                  self.p[2][1] == 'X') or \
#                 (self.p[0][2] == 'X' and
#                  self.p[1][2] == 'X' and
#                  self.p[2][2] == 'X'):
#             return 'X'
#         elif (self.p[0][0] == '0' and
#               self.p[0][1] == '0' and
#               self.p[0][2] == '0') or \
#                 (self.p[1][0] == '0' and
#                  self.p[1][1] == '0' and
#                  self.p[1][2] == '0') or \
#                 (self.p[2][0] == '0' and
#                  self.p[2][1] == '0' and
#                  self.p[2][2] == '0') or \
#                 (self.p[0][0] == '0' and
#                  self.p[1][1] == '0' and
#                  self.p[2][2] == '0') or \
#                 (self.p[0][2] == '0' and
#                  self.p[1][1] == '0' and
#                  self.p[2][0] == '0') or \
#                 (self.p[0][0] == '0' and
#                  self.p[1][0] == '0' and
#                  self.p[2][0] == '0') or \
#                 (self.p[0][1] == '0' and
#                  self.p[1][1] == '0' and
#                  self.p[2][1] == '0') or \
#                 (self.p[0][2] == '0' and
#                  self.p[1][2] == '0' and
#                  self.p[2][2] == '0'):
#             return '0'
#         elif '-' not in self.p[0] and \
#                 '-' not in self.p[1] and \
#                 '-' not in self.p[2]:
#             return 'D'
#         else:
#             return 'None'
 
#     def make_move(self, row, col):
#         if self.p[row - 1][col - 1] == '-':
#             self.n += 1
#             self.p[row - 1][col - 1] = self.list[self.n % 2]
#             if (self.p[0][0] == 'X' and
#                 self.p[0][1] == 'X' and
#                 self.p[0][2] == 'X') or \
#                     (self.p[1][0] == 'X' and
#                      self.p[1][1] == 'X' and
#                      self.p[1][2] == 'X') or \
#                     (self.p[2][0] == 'X' and
#                      self.p[2][1] == 'X' and
#                      self.p[2][2] == 'X') or \
#                     (self.p[0][0] == 'X' and
#                      self.p[1][1] == 'X' and
#                      self.p[2][2] == 'X') or \
#                     (self.p[0][2] == 'X' and
#                      self.p[1][1] == 'X' and
#                      self.p[2][0] == 'X') or \
#                     (self.p[0][0] == 'X' and
#                      self.p[1][0] == 'X' and
#                      self.p[2][0] == 'X') or \
#                     (self.p[0][1] == 'X' and
#                      self.p[1][1] == 'X' and
#                      self.p[2][1] == 'X') or \
#                     (self.p[0][2] == 'X' and
#                      self.p[1][2] == 'X' and
#                      self.p[2][2] == 'X'):
#                 self.end_info = 'Игра уже завершена'
#                 return 'Победил игрок X'
#             elif (self.p[0][0] == '0' and
#                   self.p[0][1] == '0' and
#                   self.p[0][2] == '0') or \
#                     (self.p[1][0] == '0' and
#                      self.p[1][1] == '0' and
#                      self.p[1][2] == '0') or \
#                     (self.p[2][0] == '0' and
#                      self.p[2][1] == '0' and
#                      self.p[2][2] == '0') or \
#                     (self.p[0][0] == '0' and
#                      self.p[1][1] == '0' and
#                      self.p[2][2] == '0') or \
#                     (self.p[0][2] == '0' and
#                      self.p[1][1] == '0' and
#                      self.p[2][0] == '0') or \
#                     (self.p[0][0] == '0' and
#                      self.p[1][0] == '0' and
#                      self.p[2][0] == '0') or \
#                     (self.p[0][1] == '0' and
#                      self.p[1][1] == '0' and
#                      self.p[2][1] == '0') or \
#                     (self.p[0][2] == '0' and
#                      self.p[1][2] == '0' and
#                      self.p[2][2] == '0'):
#                 self.end_info = 'Игра уже завершена'
#                 return 'Победил игрок 0'
#             elif '-' not in self.p[0] and \
#                     '-' not in self.p[1] and \
#                     '-' not in self.p[2]:
#                 self.end_info = 'Игра уже завершена'
#                 return 'Ничья'
#             else:
#                 return 'Продолжаем играть'
#         elif self.end_info != 0:
#             return self.end_info
#         else:
#             return 'Клетка ' + str(row) + ', ' + str(col) + ' уже занята'


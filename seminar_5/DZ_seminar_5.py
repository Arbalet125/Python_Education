# Напишите программу, удаляющую из текста все слова содержащие "абв".

# my_text = 'Текабвстовый абвбред Тест генерируетсяабв для рандомабвно программы потомуабвчто прошел этоабв успешно бреабвд'

# def delete_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = delete_some_words(my_text)
# print(my_text)

##################################################################

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Игра человек против человека:

# import random

# messages = ['Ваш ход', 'возьмите конфеты', 'сколько конфет возьмёте?', 'это всего лишь игра, не волнуйтесь', 'ну же, смелее']


# def play_game(n, m, players, messages):
#     first = random(0,100)
#     if first > 50: count = 0
#     else: count = 1
#     if n%10 == 1 and 9 > n > 10: letter = 'а'
#     elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
#     else: letter = ''
#     while n > 0:
#         print(f'{players[count%2]}, {random.choice(messages)}')
#         move = int(input())
#         if move > n or move > m:
#             print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
#             attempt = 3
#             while attempt > 0:
#                 if n >= move <= m:
#                     break
#                 print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                 move = int(input())
#                 attempt -=1
#             else: 
#                 return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         n = n - move
#         if n > 0: print(f'Осталось {n} конфет{letter}')
#         else: print('Все конфеты разобраны.')
#         count +=1
#     return players[not count%2]

# print('Привет, давайте начнем игру! Прежде всего, давайте знакомится.')

# player1 = input('Первый игрок, как к Вам можно обращаться?\n')
# player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
# players = [player1, player2]

# n = int(input('Сколько конфет будем разыгрывать?\n '))
# m = int(input('Сколько максимально будем брать конфет за один ход?\n '))

# winer = play_game(n, m, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else: print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

###

# Игра человек против бота:

# import random
# from random import randint, choice

# messages = ['Ваш ход', 'возьмите конфеты', 'сколько конфет возьмёте?', 'это всего лишь игра, не волнуйтесь', 'ну же, смелее']


# def introduce_players():
#     player1 = input('Давайте познакомися. Как Вас зовут?\n')
#     player2 = input('А как бы вы хотели, чтобы звали меня?\n')
#     print(f'В таком случае, очень приятно. Значит меня будут зовать {player2}')
#     return [player1, player2]


# def get_rules(players):
#     n = int(input('Сколько конфет будем разыгрывать?\n '))
#     m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
#     first = random(0,100)
#     if first > 50: first = 0
#     else: first = 1
#     return [n, m, int(first)]


# def play_game(rules, players, messages):
#     count = rules[2]
#     print(count)
#     if rules[0] % 10 == 1 and 9 > rules[0] > 10:
#         letter = 'а'
#     elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
#         letter = 'ы'
#     else:
#         letter = ''
#     while rules[0] > 0:
#         if not count % 2:
#             move = rules[0] % rules[1] + 1
#             print(f'Я забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > rules[0] or move > rules[1]:
#                 print(
#                     f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
#                 attempt = 3
#                 while attempt > 0:
#                     if rules[0] >= move <= rules[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
#                     move = int(input())
#                     attempt -= 1
#                 else:
#                     return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
#         rules[0] = rules[0] - move
#         if rules[0] > 0:
#             print(f'Осталось {rules[0]} конфет{letter}')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]


# players = introduce_players()
# rules = get_rules(players)

# winer = play_game(rules, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')


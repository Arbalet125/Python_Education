import random

def init(matr,a_hod):
    for i in range(0, 9):
        matr.append(str(i + 1))
        a_hod.append(i + 1)
    return

def print_pole(matr):
    print(' ___________')
    for n in range(0, 9, 3):
        lin = '| '
        for i in range(0, 3):
            lin += matr[n + i] + " | "
        print(lin)
        print('|___|___|___|')

def x_or_o():
    otv = input("кристик или нолик? ( введите X или 0) \n")
    if otv == "x":
        human = "X"
        ai = "O"
    else:
        human = "O"
        ai = "X"
    return human, ai

def hod_human(matr, human, avaible_hod):
    print("Ваш Ход - введите номер ячейки игрового поля:\n")
    x = int(input())
    while avaible_hod.count(x) == 0:
        print("Недоступное значение ячейки поля!")
        print("Ваш Ход - введите номер ячейки игрового поля:\n")
        print(avaible_hod.count(x))
        print(avaible_hod)
        x = int(input())
    matr[x-1] = human
    avaible_hod.remove(x)
    return

def hod_ai(matr, ai, avaible_hod):
    hod = random.choice(avaible_hod)
    matr[hod - 1] = ai
    avaible_hod.remove(hod)
    return

def vernut_stroka(matr, nomer):
    stroka=''
    for i in range(0, 3):
        stroka += matr[nomer*3 + i]
    return stroka

def vernut_stolbez(matr, nomer):
    stolb=''
    for i in range(nomer, 9, 3):
        stolb += matr[i]
    return stolb

def vernut_diagonal(matr, nomer):
    if nomer == 1:
        return matr[0]+matr[4]+matr[8]
    else:
        return matr[2]+matr[4]+matr[6]

def human_vinner(human, komb):
    shablon = human*3
    if komb.count(shablon)>0:
        print('Вы победили!')
        return True
    else:
        return False

def ai_vinner(ai, komb):
    shablon = ai*3
    if komb.count(shablon)>0:
        print('Победил компьютер')
        return True
    else:
        return False

def proverka(matr, human, ai):
    winner = False
    komb = []
    for i in range(0,3):
        komb.append(vernut_stolbez(matr, i))
        komb.append(vernut_stroka(matr, i))

    komb.append(vernut_diagonal(matr, 1))
    komb.append(vernut_diagonal(matr, 2))

    winner = human_vinner(human, komb) or ai_vinner(ai, komb)
    return winner

def main():
    pole = []
    avaible_hod = []

    init(pole,avaible_hod)
    print_pole(pole)
    human, ai = x_or_o()

    i=1
    while not proverka(pole, human, ai):
        if len(avaible_hod) == 0:
            print('Ничья!')
            break
        if i == 1:
            i=2
            if human == 'X':
                hod_human(pole, human, avaible_hod)
            else:
                hod_ai(pole, ai, avaible_hod)
        else:
            i=1
            if ai == 'O':
                hod_ai(pole, ai, avaible_hod)
            else:
                hod_human(pole, human, avaible_hod)

        print_pole(pole)


if __name__ == '__main__':
    main()

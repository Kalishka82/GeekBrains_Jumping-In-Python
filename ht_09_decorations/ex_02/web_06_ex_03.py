# Задание No3
# 📌 Улучшаем задачу 2.
# 📌 Добавьте возможность запуска функции “угадайки” из модуля в командной строке
# терминала.
# 📌 Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# 📌 Для преобразования строковых аргументов командной строки в числовые
# параметры используйте генераторное выражение.

from random import randint as rnd
from sys import argv

__all__ = ['get_random_num']

START = 0
STOP = 100
AMOUNT = 4


def get_random_num(start=START, end=STOP, amount=AMOUNT):
    flag = False
    num = rnd(start, end)
    while amount > 0:
        num_user = int(input('Введите число: '))
        if num_user == num:
            print('Число угадано!')
            flag = True
            break
        elif num_user < num:
            print('Больше')
        else:
            print('Меньше')
        amount -= 1
    else:
        print('Попытки закончились. Число НЕ угадано')

    return flag


if __name__ == '__main__':
    name, *param = argv
    print(get_random_num(*(int(elem) for elem in param)))

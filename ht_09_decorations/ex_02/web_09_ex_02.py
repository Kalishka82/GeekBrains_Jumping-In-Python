# Задание No2
# 📌 Дорабатываем задачу 1.
# 📌 Превратите внешнюю функцию в декоратор.
# 📌 Он должен проверять входят ли переданные в функцию-угадайку числа в
# диапазоны [1, 100] и [1, 10].
# 📌 Если не входят, вызывать функцию со случайными числами из диапазонов.

import random
from functools import wraps
from typing import Callable

__all__ = ['deco', 'guess_num']


def deco(func: Callable) -> Callable[[int, int], None]:
    min_num = min_try = 1
    max_num = 100
    max_try = 10

    @wraps(func)
    def wrapper(secret_num: int, guess_try: int, *args, **kwargs):
        if not min_num <= secret_num <= max_num:
            secret_num = random.randint(min_num, max_num + 1)
        if not min_try <= guess_try <= max_try:
            guess_try = random.randint(min_try, max_try + 1)
        return func(secret_num, guess_try, *args, **kwargs)
    return wrapper


@deco
def guess_num(secret_num: int, quess_try: int):
    for i in range(1, quess_try + 1):
        answer = int(input(f'Номер попытки: {i}. \n'
                           f'Угадайте число от 1 до 100: '))
        if answer == secret_num:
            print('Число угадано!')
            break
        elif answer > secret_num:
            print('Меньше ')
        else:
            print('Больше')


if __name__ == '__main__':
    guess_num(15, 4)

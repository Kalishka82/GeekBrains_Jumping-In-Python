# Задание No3
# 📌 Написать функцию в шахматный модуль.
# 📌 Использовать генератор случайных чисел для случайной расстановки ферзей в
# задаче выше.
# 📌 Проверить различные случайные варианты и вывести 4 успешных расстановки.

from random import randint

__all__ = ['set_queens', 'isCapture', 'show_success_cases']

N = 8
NUM_CASES = 4

x, y = [0] * N, [0] * N


def set_queens(n=N):
    for i in range(n):
        x[i], y[i] = randint(1, N + 1), randint(1, N + 1)
    return x, y


def isCapture(n=N):
    set_queens(n)
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] or y[i] == y[j] or \
                    abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False
            else:
                return True


def show_success_cases(cases=NUM_CASES):
    success_cases = []
    while cases > 0:
        if isCapture():
            success_cases.append([*zip(x, y)])
            cases -= 1
    return success_cases


if __name__ == '__main__':
    for i, coord_list in enumerate(show_success_cases(), start=1):
        print(f'{i}: {coord_list}')

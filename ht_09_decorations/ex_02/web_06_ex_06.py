# Задание No6
# 📌 Добавьте в модуль с загадками функцию, которая принимает на вход строку
# (текст загадки) и число (номер попытки, с которой она угадана).
# 📌 Функция формирует словарь с информацией о результатах отгадывания.
# 📌 Для хранения используйте защищённый словарь уровня модуля.
# 📌 Отдельно напишите функцию, которая выводит результаты угадывания из
# защищённого словаря в удобном для чтения виде.
# 📌 Для формирования результатов используйте генераторное выражение.

__all__ = ['puzzle', 'storage', 'show_stat']

_data = {}


def puzzle(puzzle_text: str, answers: list[str], trials: int):
    print(puzzle_text)

    try_count = 0
    while trials > 0:
        current_try = input(f'Осталось попыток: {trials}. Ваш ответ: ')
        if current_try in answers:
            return try_count
        try_count += 1
        trials -= 1
    else:
        return trials


def storage(trial_amount: int = 3):
    puzzle_dict = {
        'Загадка': ['да', 'конечно'],
        'Еще загадка': ['нет', 'наверное'],
        'Ну и еще одна': ['где', 'что'],
    }

    for puzzle_text, answer_text in puzzle_dict.items():
        puzzle_res = puzzle(puzzle_text, answer_text, trial_amount)
        add_stat(puzzle_text, puzzle_res)
        # print(puzzle_res)


def add_stat(puzzle_text: str, try_count: int):
    _data.update({puzzle_text: try_count})


def show_stat():
    print('Статистика отгадывания: ')
    output = '\n'.join((f'Загадка {puzzle_text}.' 
                        f'{f"Угадана с {trial_count} попытки." if trial_count > 0 else "Не угадана."}'
                        for puzzle_text, trial_count in _data.items()))
    print(output)


if __name__ == '__main__':
    storage()
    show_stat()

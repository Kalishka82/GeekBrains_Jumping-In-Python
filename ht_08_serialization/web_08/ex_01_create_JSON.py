# Задание No1
# 📌 Вспомнить задачу 3 из прошлого семинара. Мы сформировали текстовый файл с
# псевдоименами и произведением чисел.
# 📌 Написать функцию, которая создаёт из созданного ранее файла новый с данными
# в формате JSON.
# 📌 Имена писать с большой буквы.
# 📌 Каждую пару сохранять с новой строки.

import json

__all__ = ['create_json']

path_file = '/Users/kalishka82/PyCharmProjects/GB_Jumping_In_Python/web_07_files/ex_03_result.txt'
path_json = 'ex_08_result.json'


def create_json(path_init: str, path_to_json: str) -> None:
    res_dict = {}

    with open(path_init, 'r', encoding='utf-8') as f_read:
        for line in f_read:
            name, num = line.split('|')
            res_dict[name.capitalize()] = float(num)

    with open(path_to_json, 'w', encoding='utf-8') as f_write:
        json.dump(res_dict, f_write, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    create_json(path_file, path_json)

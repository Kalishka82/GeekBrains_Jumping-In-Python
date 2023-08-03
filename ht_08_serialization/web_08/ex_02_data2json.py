# Задание No2
# 📌 Написать функцию, которая в бесконечном цикле запрашивает имя, личный
# идентификатор и уровень доступа (от 1 до 7).
# 📌 После каждого ввода добавлять новую информацию в JSON файл.
# 📌 Пользователи группируются по уровню доступа.
# 📌 Идентификатор пользователя выступает ключём для имени.
# 📌 Убедиться, что все идентификаторы уникальны независимо от уровня доступа.
# 📌 При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
import os.path

__all__ = ['data2json']

json_file = 'ex_02.json'


def data2json(path_file):
    user_ids = set()
    if os.path.exists(path_file):
        with open(path_file, 'r', encoding='utf-8') as data_file:
            data = json.load(data_file)
            for user in data.values():
                user_ids.update(user.keys())
    else:
        data = {str(access_level): dict() for access_level in range(1, 8)}

    while True:
        name = input('Введите имя: ')
        if not name:
            break
        id = input('Введите ID: ')
        access_level = input('Введите уровень доступа: ')
        if id in user_ids:
            continue
        data[access_level][id] = name
        with open(json_file, 'w', encoding='utf-8') as data_file:
            json.dump(data, data_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    data2json(json_file)

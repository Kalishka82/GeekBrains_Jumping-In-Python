# Задание No4
# 📌 Прочитать созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Дополнить id до 10 цифр незначащими нулями.
# 📌 В именах первую букву сделать прописной.
# 📌 Добавить поле хеш на основе имени и идентификатора.
# 📌 Получившиеся записи сохранить в json файл, где каждая строка csv файла
# представлена как отдельный json словарь.
# 📌 Имя исходного и конечного файлов передавать как аргументы функции.

import csv
import json

__all__ = ['csv2json']

csv_file = 'ex_03.csv'
json_file = 'ex_04.json'


def csv2json(csv_path: str, json_path: str) -> None:
    with open(csv_path, 'r', encoding='utf-8') as f_csv:
        csv_reader = csv.reader(f_csv, dialect='excel')
        data = []
        for i, row in enumerate(csv_reader):
            if i:
                access_level, user_id, name = row
                user_data: dict = {'access_level': int(access_level),
                                   'user_id': f'{int(user_id):010}',
                                   'name': name.capitalize(),
                                   'hash': hash((user_id, name))}
                data.append(user_data)

        with open(json_path, 'w', encoding='utf-8') as f_json:
            json.dump(data, f_json, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    csv2json(csv_file, json_file)

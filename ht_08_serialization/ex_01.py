# Задание No1
# 📌 Написать функцию, которая получает на вход директорию и рекурсивно обходит её и все
# вложенные директории. Результаты обхода сохранить в файлы json, csv и pickle.
# 📌 Для дочерних объектов указать родительскую директорию.
# 📌 Для каждого объекта указать файл это или директория.
# 📌 Для файлов - сохранить его размер в байтах, а для директорий - размер файлов
# в ней с учётом всех вложенных файлов и директорий.
import csv
import json
import os
import pickle

__all__ = ['get_dir_info']


def get_dir_info(directory: str = '.') -> None:
    dir_info = []
    for root_dir, dirs, files in os.walk(directory):
        dir_size = 0
        for file in files:
            file_path = os.path.join(root_dir, file)
            file_size = os.path.getsize(file_path)
            dir_size += file_size
            dir_info.append({'path': file_path,
                             'root_dir': root_dir,
                             'type': 'file',
                             'size': file_size})
        dir_info.append({'path': root_dir,
                         'root_dir': os.path.dirname(root_dir),
                         'type': 'dir',
                         'size': dir_size})

    with open('dir_info.json', 'w', encoding='utf-8') as f_json:
        json.dump(dir_info, f_json, indent=2)

    headers = dir_info[0].keys()
    with open('dir_info.csv', 'w', encoding='utf-8') as f_csv:
        csv_writer = csv.DictWriter(f_csv, fieldnames=headers, dialect='excel',
                                    quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(dir_info)

    with open('dir_info.pickle', 'wb') as f_pickle:
        pickle.dump(dir_info, f_pickle)


if __name__ == '__main__':
    get_dir_info()

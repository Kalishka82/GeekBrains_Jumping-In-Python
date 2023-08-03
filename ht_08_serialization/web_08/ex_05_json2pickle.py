# Задание No5
# 📌 Написать функцию, которая ищет json файлы в указанной директории и сохраняет их
# содержимое в виде одноимённых pickle файлов.
import json
import os
import pickle

__all__ = ['json2pickle']

_dir = '.'


def json2pickle(dir_path) -> None:
    json_files = filter(lambda file_name: file_name[-5:] == '.json', os.listdir(dir_path))
    for file in json_files:
        with open(file, 'r', encoding='utf-8') as f_json:
            data = json.load(f_json)
        with open(f'{file[:-5]}.pickle', 'wb') as f_pickle:
            pickle.dump(data, f_pickle)


if __name__ == '__main__':
    json2pickle(_dir)

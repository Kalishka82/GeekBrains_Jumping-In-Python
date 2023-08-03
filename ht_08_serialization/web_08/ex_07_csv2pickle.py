# Задание No7
# 📌 Прочитать созданный в прошлом задании csv файл без использования csv.DictReader.
# 📌 Распечатать его как pickle строку.

import csv
import pickle

__all__ = ['csv2pickles']

pickle_file = 'ex_06.csv'


def csv2pickles(pickle_path: str) -> None:
    with open(pickle_path, 'r', encoding='utf-8') as f_csv:
        csv_reader = csv.reader(f_csv, dialect='excel')
        data_list = []
        headers = []
        for i, row in enumerate(csv_reader):
            if not i:
                headers = row
            else:
                row_data = {key: value for key, value in zip(headers, row)}
                data_list.append(row_data)
    print(pickle.dumps(data_list))


if __name__ == '__main__':
    csv2pickles(pickle_file)

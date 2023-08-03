# Задание No6
# 📌 Написать функцию, которая преобразует pickle файл, хранящий список словарей
# в табличный csv файл.
# 📌 Для тестирования взять pickle версию файла из задачи 4 этого семинара.
# 📌 Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import pickle

__all__ = ['pickle2csv']

pickle_file = 'ex_04.pickle'
csv_file = 'ex_06.csv'


def pickle2csv(pickle_path: str, csv_path: str):
    with open(pickle_path, 'rb') as f_pickle:
        data = pickle.load(f_pickle)
    headers = data[0].keys()

    with open(csv_path, 'w', encoding='utf-8') as f_csv:
        csv_writer = csv.DictWriter(f_csv, fieldnames=headers, dialect='excel',
                                    quoting=csv.QUOTE_NONNUMERIC)
        csv_writer.writeheader()
        csv_writer.writerows(data)


if __name__ == '__main__':
    pickle2csv(pickle_file, csv_file)

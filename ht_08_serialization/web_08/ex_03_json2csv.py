# Задание No3
# 📌 Написать функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.
import csv
import json

__all__ = ['json2csv']

json_file = 'ex_02.json'
csv_file = 'ex_03.csv'


def json2csv(json_path: str, csv_path: str) -> None:
    with open(json_path, 'r', encoding='utf-8') as f_json:
        data = json.load(f_json)
    rows = []
    for access_level, users in data.items():
        for user_id, name in users.items():
            rows.append({'access_level': int(access_level), 'id': int(user_id),
                         'name': name})
    # print(rows)

    with open(csv_path, 'w', encoding='utf-8') as f_csv:
        csv_dict = csv.DictWriter(f_csv, fieldnames=['access_level', 'id', 'name'],
                                  dialect='excel')
        csv_dict.writeheader()
        csv_dict.writerows(rows)


if __name__ == '__main__':
    json2csv(json_file, csv_file)

# Задание No6
# 📌 Создайте класс студента.
# ✔ Используя дескрипторы, проверяйте ФИО на первую заглавную букву и наличие только букв.
# ✔ Названия предметов должны загружаться из файла CSV при создании экземпляра.
# Другие предметы в экземпляре недопустимы.
# ✔ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# ✔ Также экземпляр должен сообщать средний балл по тестам для каждого предмета
# и по оценкам всех предметов вместе взятых.
import csv

_MIN_MARK = 2
_MAX_MARK = 5
_MIN_TEST_RES = 0
_MAX_TEST_RES = 100

SUBJECT_FILE = 'ex_01_subject.csv'
STUDENT_FILE = 'ex_01.student.json'


class CheckName:
    """Проверка ФИО на содержание только букв и первую заглавную"""
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: str):
        if not value.isalpha():
            return ValueError(f'"{value}" должно содержать только буквы')
        if not value.istitle():
            return ValueError(f'Первая буква в "{value}" должна быть заглавной')
        setattr(instance, self.param_name, value)


class CheckMarkTest:
    """Проверка оценок и результатов тестов на попадание в диапазон возможных"""
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if not (self.min_value <= value <= self.max_value):
            return ValueError(f'Оценка "{value}" не соответствует диапазону от {self.min_value} до {self.max_value}')
        setattr(instance, self.param_name, value)


class Student:
    first_name = CheckName()
    mid_name = CheckName()
    last_name = CheckName()
    marks = list[CheckMarkTest(_MIN_MARK, _MAX_MARK)]
    tests = list[CheckMarkTest(_MIN_TEST_RES, _MAX_TEST_RES)]

    def __init__(self, first_name: str, mid_name: str, last_name: str):
        self.first_name = first_name
        self.mid_name = mid_name
        self.last_name = last_name

    @staticmethod
    def calculate_averages():
        dict_averages = {}
        with open(SUBJECT_FILE, 'r', encoding='utf-8', newline='') as f:
            filereader = csv.DictReader(f, delimiter=';')
            for line in filereader:
                marks = list(map(int, line['Marks'].split()))
                tests = list(map(int, line['Tests'].split()))
                aver_mark = sum(marks) / len(marks)
                aver_test = sum(tests) / len(tests)
                dict_averages[line['Subject']] = ('%.2f' % aver_mark, '%.2f' % aver_test)

            for key, value in dict_averages.items():
                print(f'{key}: средний балл по тестам={value[1]}')

            sum_marks = sum(float(key[0]) for _, key in dict_averages.items())
            aver_mark_all_subj = round(sum_marks / len(dict_averages), 2)
            print(f'Средняя оценка по всем предметам={aver_mark_all_subj}')


class Main:
    stud_1 = Student('Иван', 'ИВАНович', 'Петров123')
    print(stud_1.__dict__)
    stud_1.calculate_averages()


if __name__ == '__main__':
    Main()

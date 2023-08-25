from ex_01_Matrix import Matrix


class MyException(Exception):
    pass


class TwoWayEqualSizeException(MyException):
    def __init__(self, first: Matrix, second: Matrix):
        self.first = first
        self.second = second

    def __str__(self):
        return f'Размерности матриц [{self.first.rows} X {self.second.rows}] и ' \
               f'[{self.first.clmns} X {self.second.clmns}] не совпадают!'


class OneWayEqualSizeException(MyException):
    def __init__(self, first: Matrix, second: Matrix):
        self.first = first
        self.second = second

    def __str__(self):
        return f'{self.first.clmns} != {self.second.rows} - количество столбцов одной матрицы и ' \
               f'количество строк другой не равны. Операция умножения невозможна!'

# Задание No1
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода.
# Например, нельзя создавать прямоугольник со сторонами отрицательной длины.

# from ex_01_MyException import TwoWayEqualSizeException, OneWayEqualSizeException


class Matrix:
    _matrix: list[list[int | float]] = None
    _rows: int = None
    _clmns: int = None

    def __init__(self, matrix: list[list[int | float]]) -> None:
        """
        :param matrix: [[int | float]]  -> матрица размерностью rows X clmns
        :param rows: int                -> a number of rows
        :param clmns: int               -> a number of columns
        """
        self._matrix = matrix
        self._rows = len(matrix)
        self._clmns = len(matrix[0])

    @property
    def rows(self):
        return self._rows

    @property
    def clmns(self):
        return self._clmns

    def __repr__(self):
        """Строка-представление объекта класса Matrix"""
        return f'Matrix({self._matrix})'

    def _eq_len(self, other):
        """Метод сравнивает размерности матриц в двух направлениях"""
        return self._rows == other._rows and \
               self._clmns == other._clmns

    def __eq__(self, other):
        """ Метод сравнивает матрицы ОДИНАКОВОЙ размерности:
         Матрицы равны, если равны их соответствующие элементы.
         """
        flag = True
        if self is other:
            return flag
        else:
            for i in range(self._rows):
                for j in range(self._clmns):
                    if self._matrix[i][j] != other._matrix[i][j]:
                        flag = False
                        break
        return flag

    def __add__(self, other):
        """Метод считает сумму матриц ОДИНАКОВОЙ размерности"""
        new_mtrx = [[0 for j in range(self._clmns)] for i in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._clmns):
                new_mtrx[i][j] = self._matrix[i][j] + other._matrix[i][j]
        return Matrix(new_mtrx)

    def __mul__(self, other):
        """Метод считает умножение матриц"""
        new_mtrx = [[0 for j in range(other._clmns)] for i in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._clmns):
                for k in range(self._clmns):
                    new_mtrx[i][j] += self._matrix[i][k] * other._matrix[k][j]
        return Matrix(new_mtrx)

#  Задание No2
# 📌 Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix:
    ERROR_1 = 'Размерности матриц не совпадают!'
    ERROR_2 = 'Кол-во рядов одной матрицы и кол-во строк другой не совпадают!'

    _matrix: list[list[int | float]] = None
    _rows: int = None
    _clmns: int = None

    def __init__(self, matrix: list[list[int | float]]) -> None:
        """
        :param matrix: [[int | float]]  -> матрица размерностью clmns X rows
        :param rows: int                -> a rows number
        :param clmns: int               -> a columns number
        """
        self._matrix = matrix
        self._rows = len(matrix)
        self._clmns = len(matrix[0])

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
        if not Matrix._eq_len(self, other):
            flag = self.ERROR_1
        else:
            flag = True
            if self is other:
                return flag
            else:
                for j in range(self._rows):
                    for i in range(self._clmns):
                        if self._matrix[j][i] != other._matrix[j][i]:
                            flag = False
                            break
        return flag

    def __gt__(self, other):
        """ Метод сравнивает матрицы ОДИНАКОВОЙ размерности:
         Будем считать, что одна матрица больше другой, если все элементы одной больше
         соответствущих элементов другой.
         """
        if not Matrix._eq_len(self, other):
            flag = self.ERROR_1
        else:
            flag = True
            if self is other:
                return flag
            else:
                for j in range(self._rows):
                    for i in range(self._clmns):
                        if self._matrix[j][i] > other._matrix[j][i]:
                            flag = False
                            break
        return flag

    def __le__(self, other):
        """ Метод сравнивает матрицы ОДИНАКОВОЙ размерности:
         Будем считать, что одна матрица НЕ больше другой, если все элементы одной НЕ больше
         соответствущих элементов другой.
         """
        if not Matrix._eq_len(self, other):
            flag = self.ERROR_1
        else:
            flag = True
            if self is other:
                return flag
            else:
                for j in range(self._rows):
                    for i in range(self._clmns):
                        if self._matrix[j][i] <= other._matrix[j][i]:
                            flag = False
                            break
        return flag

    def __add__(self, other):
        """Метод считает сумму матриц ОДИНАКОВОЙ размерности"""
        if not Matrix._eq_len(self, other):
            return print(self.ERROR_1)
        new_mtrx = [[0 for _ in range(self._clmns)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._clmns):
                new_mtrx[j][i] = self._matrix[j][i] + other._matrix[j][i]
        return Matrix(new_mtrx)

    def __mul__(self, other):
        """Метод считает умножение матриц"""
        if self._clmns != other._rows:
            return print(self.ERROR_2)
        new_mtrx = [[0 for _ in range(self._clmns)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(self._clmns):
                new_mtrx[j][i] = self._matrix[j][i] + other._matrix[i][j]
        return Matrix(new_mtrx)


def main():
    mtrx_1 = Matrix([[0, 1, 2, 3], [4, 5, 6, 7]])
    mtrx_2 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
    mtrx_3 = Matrix([[2, 3, 4, 5], [6, 7, 8, 9]])
    mtrx_4 = Matrix([[0, 1, 2, 3], [4, 5, 6, 7]])

    mtrxs = (mtrx_1, mtrx_2, mtrx_3, mtrx_4)
    for elem in mtrxs:
        print(repr(elem))

    print(mtrx_1 == mtrx_2, mtrx_1 == mtrx_3, mtrx_1 == mtrx_4)
    print(mtrx_1 != mtrx_2, mtrx_1 != mtrx_3, mtrx_1 != mtrx_4)
    print(mtrx_1 > mtrx_2, mtrx_1 > mtrx_3, mtrx_1 > mtrx_4)
    print(mtrx_1 >= mtrx_2, mtrx_1 >= mtrx_3, mtrx_1 >= mtrx_4)
    print(mtrx_1 < mtrx_2, mtrx_1 < mtrx_3, mtrx_1 < mtrx_4)
    print(mtrx_1 <= mtrx_2, mtrx_1 <= mtrx_3, mtrx_1 <= mtrx_4)
    print('---------')

    print(repr(mtrx_1 + mtrx_2))
    print(repr(mtrx_1 + mtrx_3))
    print('---------')

    print(repr(mtrx_1 * mtrx_2))
    print(repr(mtrx_1 * mtrx_3))


if __name__ == '__main__':
    main()

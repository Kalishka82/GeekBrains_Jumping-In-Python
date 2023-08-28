# Задание No1
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
#   ✔ doctest,
#   ✔ unittest,
#   ✔ pytest.

import doctest
from ht_14_tests.ex_01_Matrix import Matrix

mtrx_1 = Matrix([[2, 1], [-3, 0], [4, -1]])
mtrx_2 = Matrix([[5, -1, 6], [-3, 0, 7]])
mtrx_3 = Matrix([[2, 1], [-3, 0], [4, -1]])
mtrx_4 = Matrix([[5, 1, 6], [3, 0, 7]])


def test_matrix():
    """
    >>> print(repr(mtrx_1))
    Matrix([[2, 1], [-3, 0], [4, -1]])
    >>> print(Matrix._eq_len(mtrx_1, mtrx_3))
    True
    >>> print(Matrix._eq_len(mtrx_1, mtrx_2))   
    False
    >>> print(mtrx_1 == mtrx_3)
    True
    >>> print(mtrx_2 == mtrx_4)
    False
    >>> print(repr(mtrx_1 + mtrx_3))
    Matrix([[4, 2], [-6, 0], [8, -2]])
    >>> print(repr(mtrx_1 * mtrx_2))
    Matrix([[7, -2, 19], [-15, 3, -18], [23, -4, 17]])
    """


if __name__ == '__main__':
    doctest.testmod(verbose=True)

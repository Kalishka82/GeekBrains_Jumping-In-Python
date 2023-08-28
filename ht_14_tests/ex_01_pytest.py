# Задание No1
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
#   ✔ doctest,
#   ✔ unittest,
#   ✔ pytest.

import pytest
from ht_14_tests.ex_01_Matrix import Matrix


@pytest.fixture()
def set_matrix():
    mtrx_1 = Matrix([[2, 1], [-3, 0], [4, -1]])
    mtrx_2 = Matrix([[5, -1, 6], [-3, 0, 7]])
    mtrx_3 = Matrix([[2, 1], [-3, 0], [4, -1]])
    mtrx_4 = Matrix([[5, 1, 6], [3, 0, 7]])
    return mtrx_1, mtrx_2, mtrx_3, mtrx_4


def test_create(set_matrix):
    mtrx_1, _, _, _ = set_matrix
    assert mtrx_1 == Matrix([[2, 1], [-3, 0], [4, -1]])


def test_eq_len(set_matrix):
    mtrx_1, _, mtrx_3, _ = set_matrix
    assert Matrix._eq_len(mtrx_1, mtrx_3) is True


def test_not_eq_len(set_matrix):
    mtrx_1, mtrx_2, _, _ = set_matrix
    assert Matrix._eq_len(mtrx_1, mtrx_2) is False


def test_eq(set_matrix):
    mtrx_1, _, mtrx_3, _ = set_matrix
    assert mtrx_1 == mtrx_3


def test_not_eq(set_matrix):
    _, mtrx_2, _, mtrx_4 = set_matrix
    assert mtrx_2 != mtrx_4


def test_add(set_matrix):
    mtrx_1, _, mtrx_3, _ = set_matrix
    assert mtrx_1 + mtrx_3 == Matrix([[4, 2], [-6, 0], [8, -2]])


def test_mul(set_matrix):
    mtrx_1, mtrx_2, _, _ = set_matrix
    assert mtrx_1 * mtrx_2 == Matrix([[7, -2, 19], [-15, 3, -18], [23, -4, 17]])


if __name__ == '__main__':
    pytest.main()

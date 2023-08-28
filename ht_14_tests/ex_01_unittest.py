# Задание No1
# 📌 Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# 📌 Напишите к ним тесты.
# 📌 2-5 тестов на задачу в трёх вариантах:
#   ✔ doctest,
#   ✔ unittest,
#   ✔ pytest.

import unittest
from ht_14_tests.ex_01_Matrix import Matrix


class TestMatrix(unittest.TestCase):
    def setUp(self):
        self.mtrx_1 = Matrix([[2, 1], [-3, 0], [4, -1]])
        self.mtrx_2 = Matrix([[5, -1, 6], [-3, 0, 7]])
        self.mtrx_3 = Matrix([[2, 1], [-3, 0], [4, -1]])
        self.mtrx_4 = Matrix([[5, 1, 6], [3, 0, 7]])

    def test_create(self):
        self.assertEqual(self.mtrx_1, Matrix([[2, 1], [-3, 0], [4, -1]]))

    def test_eq_len(self):
        self.assertTrue(Matrix._eq_len(self.mtrx_1, self.mtrx_3))

    def test_not_eq_len(self):
        self.assertFalse(Matrix._eq_len(self.mtrx_1, self.mtrx_2))

    def test_eq(self):
        self.assertTrue(self.mtrx_1, self.mtrx_3)

    def test_not_eq(self):
        self.assertNotEqual(self.mtrx_2, self.mtrx_4)

    def test_add(self):
        self.assertEqual(self.mtrx_1 + self.mtrx_3, Matrix([[4, 2], [-6, 0], [8, -2]]))

    def test_mul(self):
        self.assertEqual(self.mtrx_1 * self.mtrx_2, Matrix([[7, -2, 19], [-15, 3, -18], [23, -4, 17]]))


if __name__ == '__main__':
    unittest.main()

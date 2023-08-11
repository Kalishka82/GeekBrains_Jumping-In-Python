# Задание No2
# 📌 Взять 1-3 любые задачи из прошлых семинаров (например, сериализация данных),
# которые уже решали:
# ○ Превратить функции в методы класса, а параметры в свойства.
# ○ Задачи должны решаться через вызов методов экземпляра.


class MyMatrix:
    def __init__(self, matrix: [[int]]):
        self.matrix = matrix

    def print_matrix(self, t_matrix=None) -> None:
        if t_matrix is None:
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    print(self.matrix[i][j], end=' ')
                print()
            print()
        else:
            for i in range(len(t_matrix)):
                for j in range(len(t_matrix[0])):
                    print(t_matrix[i][j], end=' ')
                print()
            print()

    def transpose_matrix(self) -> [[int]]:
        t_matrix = [[0] * len(self.matrix) for i in range(len(self.matrix[0]))]
        for i in range(len(t_matrix)):
            for j in range(len(t_matrix[0])):
                t_matrix[i][j] = self.matrix[j][i]
        return t_matrix


def main():
    m_1 = MyMatrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    m_2 = MyMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    matrixes = (m_1, m_2)
    for elem in matrixes:
        elem.print_matrix()
        elem.print_matrix(elem.transpose_matrix())


if __name__ == '__main__':
    main()

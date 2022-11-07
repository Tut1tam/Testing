from matrix import Matrix
import unittest


class TestMatrix(unittest.TestCase):

    # Тест кейс на нормальные матричные операции
    def test__normal_matrix(self):
        self.matrix = Matrix([[1, 2, 3], [4, 5, 6]], [[9, 8, 7], [6, 5, 4]])
        mat1, mat2 = [[1, 2, 3], [4, 5, 6]], [[9, 8, 7], [6, 5, 4]]
        res, dif = [[10, 10, 10], [10, 10, 10]], [[-8, -6, -4], [-2, 0, 2]]
        self.assertEqual(
            self.matrix.draw_matrix(),
            f"Ваша первая матрица:\n{mat1}\nВаша вторая матрица:\n{mat2}",
        )
        self.assertEqual(self.matrix.sum_matrix(), f"Матрица суммы:\n{res}")
        self.assertEqual(self.matrix.dif_matrix(), f"Матрица разности:\n{dif}")

    # Тест кейс на матричные операции с матрицами разного размера
    def test__not_normal_matrix(self):
        self.matrix = Matrix([[1, 2, 3], [4, 5, 6]], [[9, 8, 7], [9, 8, 7], [9, 8, 7]])
        mat1, mat2 = [[1, 2, 3], [4, 5, 6]], [[9, 8, 7], [9, 8, 7], [9, 8, 7]]
        self.assertEqual(
            self.matrix.draw_matrix(),
            f"Ваша первая матрица:\n{mat1}\nВаша вторая матрица:\n{mat2}",
        )
        self.assertEqual(
            self.matrix.sum_matrix(),
            f"Матрицы должны быть одинаковых размеров, для того чтобы их можно было сложить!",
        )
        self.assertEqual(
            self.matrix.dif_matrix(),
            f"Матрицы должны быть одинаковых размеров, для того чтобы их можно было вычесть!",
        )


if __name__ == "__main__":
    unittest.main()

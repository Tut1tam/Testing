class Matrix:
    mat1, mat2 = [], []
    h1, h2 = 0, 0

    def __init__(self, mat1, mat2):
        self.mat1, self.mat2 = mat1, mat2
        self.h1, self.h2 = len(mat1), len(mat2)

    def sum_matrix(self):
        mat1, mat2 = self.mat1, self.mat2
        res = []
        if self.h1 == self.h2:
            res = [
                [mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))]
                for i in range(len(mat1))
            ]
            return f"Матрица суммы:\n{res}"
        else:
            return f"Матрицы должны быть одинаковых размеров, для того чтобы их можно было сложить!"

    def dif_matrix(self):
        mat1, mat2 = self.mat1, self.mat2
        res = []
        if self.h1 == self.h2:
            res = [
                [mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))]
                for i in range(len(mat1))
            ]
            return f"Матрица разности:\n{res}"
        else:
            return f"Матрицы должны быть одинаковых размеров, для того чтобы их можно было вычесть!"

    def draw_matrix(self):
        return f"Ваша первая матрица:\n{self.mat1}\nВаша вторая матрица:\n{self.mat2}"

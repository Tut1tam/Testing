from math import cos, pi
from re import L
from scipy import integrate


class Integral:
    n = 0
    x1, x0 = 0, 0

    def __init__(self, n, x1, x0):
        self.n = n
        self.x1, self.x0 = x1, x0

    def calc_integral(self):
        def func(x):
            return x + self.n
        ans, err = integrate.quad(func, self.x1, self.x0)
        return f'Результат вычисления интеграла ∫(x + {self.n})dx = {ans}'

    def draw_integral(self):
        return f'Ваш интеграл - ∫(x + {self.n})dx, с границами от {self.x1} до {self.x0}'
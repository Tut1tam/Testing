# Класс для решения уравнений
# a*x^3 + b*x^2 + c*x + d = 0
class Equation:
    a, b, c, d = 0, 0, 0, 0
    type = None

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d


    # c*x + d = 0
    def calc_lin(self):
        c, d = self.c, self.d
        if c != 0:
            return -d/c
        else:
            return f'Уравнение {c}*x + {d} = 0 не имеет решений'

    # b*x^2 + c*x + d = 0
    def calc_quad(self):
        b, c, d = self.b, self.c, self.d
        dis = c**2 - 4*b*d
        if dis >= 0:
            x1 = (-c + dis**(1/2))/2*b
            x2 = (-c - dis**(1/2))/2*b
            sol = {x1, x2}
            return sol
        elif dis < 0:
            return 'Действительных корней нет'

    def calc_cub(self):
        return 'К сожалению, мы пока не умеем решать такие уравнения :('

    # a*x^3 + b*x^2 + c*x + d = 0
    def calc_type(self):
        a, b = self.a, self.b
        if a == 0:
            if b == 0:
                return 'Линейное'
            else:
                return 'Квадратное'
        else:
            return 'Кубическое'

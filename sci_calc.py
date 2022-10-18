from equation import Equation
from matrix import Matrix
from integral import Integral


def equation():
    print('Введите коэффициенты(A,B,C,D) Вашего уравнения вида - A*x^3 + B*x^2 + C*x + D = 0\n')
    a, b, c, d = float(input()), float(input()), float(input()), float(input())
    equation = Equation(a, b, c, d)
    type = equation.calc_type()
    print(f'Вы ввели {type} уравнение вида {a}*x^3 + {b}*x^2 + {c}*x + {d} = 0')
    match type:
        case 'Линейное':
            print(f'Решение вашего линейного уравнения {c}*x + {d} = 0\nX = {equation.calc_lin()}')
        case 'Квадратное':
            print(f'Решение вашего квадратного уравнения {b}*x^2 + {c}*x + {d} = 0\nX = {equation.calc_quad()}')
        case _:
            print(f'К сожалению, мы пока не умеем решать такие уравнения {a}*x^3 + {b}*x^2 + {c}*x + {d} = 0\n')


def matrix():
    mat1, mat2 = [[1, 2, 3], [4, 5, 6]], [[9, 8, 7], [6, 5, 4]]
    matrix = Matrix(mat1, mat2)
    matrix.draw_matrix()
    matrix.sum_matrix()
    matrix.dif_matrix()


def integral():
    print(f'Введите N вашей функции f(x + N) интеграла вида: ∫f(x)dx\nВведите границы интегрирования x1, x0')
    n, x1, x0 = input().split(' ')
    n, x1, x0 = float(n), float(x1), float(x0)
    integral = Integral(n, x1, x0)
    integral.calc_integral()

def main():
    print('Выбирете нужную функцию из списка:\n')
    print('1. Решение уравнений\n2. Решение матричных операций\n3. Решение интегралов\n')
    match input():
        case '1':
            equation()
        case '2':
            matrix()
        case '3':
            integral()
        case _:
            print(f'К сожалению мы пока не умеем это делать :(')


if __name__ == '__main__':
    main()

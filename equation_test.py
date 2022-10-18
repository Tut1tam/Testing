from equation import Equation
import unittest


class TestEquation(unittest.TestCase):

    # Тест кейс на решение линейных уравнений
    def test_lin(self):
        self.equation = Equation(0, 0, 2, 4)
        self.assertEqual(self.equation.calc_type(), 'Линейное')
        self.assertEqual(self.equation.calc_lin(), -2)
        
    # Тест кейс на решение линейных уравнений с 0х    
    def test_lin_dev_null(self):
        self.equation = Equation(0, 0, 0, 4)
        self.assertEqual(self.equation.calc_type(), 'Линейное')
        self.assertEqual(self.equation.calc_lin(), 'Уравнение 0*x + 4 = 0 не имеет решений')

    # Тест кейс на решение квадратных уравнений
    def test_quad(self):
        self.equation = Equation(0, 2, 2, -4)
        self.assertEqual(self.equation.calc_type(), 'Квадратное')
        self.assertEqual(self.equation.calc_quad(), {-8.0, 4.0})

    # Тест кейс на решение квадратных уравнений без действительных корней
    def test_quad_without_sol(self):
        self.equation = Equation(0, 2, 2, 4)
        self.assertEqual(self.equation.calc_type(), 'Квадратное')
        self.assertEqual(self.equation.calc_quad(), 'Действительных корней нет')

    # Тест кейс на решение кубических уравнений
    def test_cub(self):
        self.equation = Equation(1, 2, 2, 4)
        self.assertEqual(self.equation.calc_type(), 'Кубическое')
        self.assertEqual(self.equation.calc_cub(), 'К сожалению, мы пока не умеем решать такие уравнения :(')


if __name__ == '__main__':
    unittest.main()

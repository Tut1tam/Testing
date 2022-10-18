from integral import Integral
import unittest


class TestIntegral(unittest.TestCase):

    # Тест кейс на решение интегралов
    def test__integral(self):
        self.integral = Integral(5, 0, 10)
        self.assertEqual(self.integral.draw_integral(), f'Ваш интеграл - ∫(x + 5)dx, с границами от 0 до 10')
        self.assertEqual(self.integral.calc_integral(), f'Результат вычисления интеграла ∫(x + 5)dx = 100.0\n')        


if __name__ == '__main__':
    unittest.main()

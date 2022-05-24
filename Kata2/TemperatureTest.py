import unittest
import Temperature

class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(6, Temperature.Calculate(3,Temperature.TemperatureScale.Celsius, 275.15, Temperature.TemperatureScale.Kelvin,4))  # add assertion here
    def test2(self):
        self.assertEqual(10, Temperature.Calculate(5,Temperature.TemperatureScale.Kelvin, -450.67, Temperature.TemperatureScale.Farenheit,1))  # add assertion here
    def test3(self):
        self.assertEqual(8, Temperature.Calculate(10,Temperature.TemperatureScale.Farenheit, -16.6667, Temperature.TemperatureScale.Celsius,2))  # add assertion here
    def test4(self):
        self.assertEqual(3, Temperature.Calculate(6,Temperature.TemperatureScale.Celsius, 35.6, Temperature.TemperatureScale.Farenheit,3))  # add assertion here
    def test5(self):
        self.assertEqual(15, Temperature.Calculate(10, Temperature.TemperatureScale.Kelvin,-268.15 , Temperature.TemperatureScale.Celsius,1))  # add assertion here
    def test6(self):
        self.assertEqual(13, Temperature.Calculate(20, Temperature.TemperatureScale.Farenheit,259.261 , Temperature.TemperatureScale.Kelvin,2))  # add assertion here
    def test7(self):
        self.assertEqual(5, Temperature.Calculate(10, Temperature.TemperatureScale.Kelvin, -456.07,Temperature.TemperatureScale.Farenheit, 3))
    def test8(self):
        self.assertEqual(25, Temperature.Calculate(5, Temperature.TemperatureScale.Celsius, 278.15,Temperature.TemperatureScale.Kelvin, 4))
    def test9(self):
         self.assertEqual("Operacion Invalida", Temperature.Calculate(5, Temperature.TemperatureScale.Celsius, 278.15,Temperature.TemperatureScale.Kelvin, 5))

    def test10(self):
        self.assertEqual("Vacio", Temperature.Calculate(0, Temperature.TemperatureScale.Celsius, 0,Temperature.TemperatureScale.Kelvin, 5))

    def test11(self):
            self.assertEqual("Vacio", Temperature.Calculate("", Temperature.TemperatureScale.Celsius, "" ,Temperature.TemperatureScale.Kelvin, 5))
        # add assertion here
    # add assertion here


if __name__ == '__main__':
    unittest.main()

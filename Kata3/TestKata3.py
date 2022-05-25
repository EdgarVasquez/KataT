import unittest
import main

class MyTestCase(unittest.TestCase):

    def test_something(self):
        self.assertEqual(10, main.Operation(5,main.TemperatureScale.Celsius,278.15,main.TemperatureScale.Kelvin,1) ) # add assertion here
    def test2(self):
        self.assertEqual(10, main.Operation(20,main.TemperatureScale.Celsius,283.15,main.TemperatureScale.Kelvin,2) ) # add assertion here
    def test3(self):
        self.assertEqual(6, main.Operation(2, main.TemperatureScale.Celsius, 276.15, main.TemperatureScale.Kelvin,3))  # add assertion here
    def test4(self):
        self.assertEqual(5, main.Operation(25,main.TemperatureScale.Celsius,278.15,main.TemperatureScale.Kelvin,4) )
        # add assertion here
    def test5(self):
        self.assertEqual(10, main.Operation(5,main.TemperatureScale.Celsius,41,main.TemperatureScale.Farenheit,1) ) # add assertion here
    def test6(self):
        self.assertEqual(10, main.Operation(20,main.TemperatureScale.Celsius,50,main.TemperatureScale.Farenheit,2) ) # add assertion here
    def test7(self):
        self.assertEqual(6, main.Operation(2, main.TemperatureScale.Celsius, 37.4, main.TemperatureScale.Farenheit,3))  # add assertion here
    def test8(self):
        self.assertEqual(5, main.Operation(25,main.TemperatureScale.Celsius,41,main.TemperatureScale.Farenheit,4) )
    def test9(self):
        self.assertEqual(10, main.Operation(5,main.TemperatureScale.Kelvin,-450.67,main.TemperatureScale.Farenheit,1) ) # add assertion here
    def test10(self):
        self.assertEqual(10, main.Operation(20,main.TemperatureScale.Kelvin,-441.67,main.TemperatureScale.Farenheit,2) ) # add assertion here
    def test11(self):
        self.assertEqual(6, main.Operation(2, main.TemperatureScale.Kelvin, -454.27, main.TemperatureScale.Farenheit,3))  # add assertion here
    def test12(self):
        self.assertEqual(5, main.Operation(25,main.TemperatureScale.Kelvin,-450.67,main.TemperatureScale.Farenheit,4) )
    def test13(self):
        self.assertEqual(10, main.Operation(5,main.TemperatureScale.Farenheit,-15,main.TemperatureScale.Celsius,1) ) # add assertion here
    def test14(self):
        self.assertEqual(10, main.Operation(20,main.TemperatureScale.Farenheit,-12.2222,main.TemperatureScale.Celsius,2) ) # add assertion here
    def test15(self):
        self.assertEqual(6, main.Operation(2, main.TemperatureScale.Farenheit, -16.111, main.TemperatureScale.Celsius,3))  # add assertion here
    def test16(self):
        self.assertEqual(5, main.Operation(25,main.TemperatureScale.Farenheit,-15,main.TemperatureScale.Celsius,4) )

    def test17(self):
        self.assertEqual("No puede ser 0", main.Operation(0, main.TemperatureScale.Farenheit, -15, main.TemperatureScale.Celsius, 4))

    def test18(self):
        self.assertEqual("Operacion invalida", main.Operation(5, main.TemperatureScale.Farenheit, -15, main.TemperatureScale.Celsius, 5))
if __name__ == '__main__':
    unittest.main()

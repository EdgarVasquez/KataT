import unittest
import Temperature
import main
from TemperatureScale import TemperatureScale

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(2, main.ToDivide(6, -16.1111, TemperatureScale.Fahrenheit,TemperatureScale.Celsius))  # add assertion here


if __name__ == '__main__':
    unittest.main()

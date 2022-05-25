from TemperatureScale import TemperatureScale
from Temperature import Temperature
def ToSum(Grade1,Grade2,scale1,scale2):
    G1 = Temperature(Grade1, scale1)
    G2 = Temperature(Grade2, scale2 )
    G3 = Temperature.__add__(G1, G2)
    return G3
def ToMultiply(Grade1,Grade2,scale1,scale2):
    G1 = Temperature(Grade1, scale1)
    G2 = Temperature(Grade2, scale2 )
    G3 = Temperature.Multiply(G1, G2)
    return G3
def ToDivide(Grade1,Grade2,scale1,scale2):
    G1 = Temperature(Grade1, scale1)
    G2 = Temperature(Grade2, scale2 )
    G3 = Temperature.Divide(G1, G2)
    return G3
def ToSubstract(Grade1,Grade2,scale1,scale2):
    G1 = Temperature(Grade1, scale1)
    G2 = Temperature(Grade2, scale2 )
    G3 = Temperature.subtract(G1, G2)
    return G3

if __name__ == '__main__':
    ToSum(6, -457.87,TemperatureScale.Kelvin,TemperatureScale.Fahrenheit)



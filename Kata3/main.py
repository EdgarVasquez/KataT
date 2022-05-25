def Operation(grade1, scale1, grade2, sacle2, operacion):
    if grade1 != 0:
        GradeResult = ConvertTemperature(sacle2, grade2, scale1)
        if operacion == 1:
            OperationResult = round(grade1 + GradeResult)
        elif operacion == 2:
            OperationResult = round(grade1 - GradeResult)
        elif operacion == 3:
            OperationResult = round(grade1 * GradeResult)
        elif operacion == 4:
            OperationResult = round(grade1 / GradeResult)
        else:
            OperationResult = "Operacion invalida"
    else:
        OperationResult = "No puede ser 0"
    return OperationResult

def ConvertTemperature(scale,grade,ScalePrincipal):
    if ScalePrincipal == "C":
        if scale == "F":
            Result = (grade - 32) * (5/9)
        elif scale == "K":
            Result = grade - 273.15
        else:
            Result = grade
    elif ScalePrincipal == "K":
        if scale == "C":
            Result = grade + 273.15
        elif scale == "F":
            Result = (grade - 32) * (5/9) + 273.15
        else:
            Result = grade
    elif ScalePrincipal == "F":
        if scale == "C":
            Result = (grade * (9/5)) + 32
        elif scale == "K":
            Result = (grade - 273.15) * (9/5) + 32
        else:
            Result = grade
    else:
        Result = "No valid"
    return  Result




class TemperatureScale:
    Kelvin = "K"
    Celsius = "C"
    Farenheit = "F"
class Temperature:

    def __init__(self, Grade , Scale):
        self.grade  = Grade
        self.scale = Scale



if __name__ == '__main__':

    T3 = Temperature.Operation(2,TemperatureScale.Kelvin, -270.15,TemperatureScale.Celsius, 3)
    print(T3)

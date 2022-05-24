def ConvertToCelsius(grade, scale):
    if scale == "F":
        result = (grade-32) * (5/9)
    elif scale == "K":
        result = (grade - 273.15)
    else:
        result = grade
    return result


def ConvertToKelvin(grade, scale):
    if scale == "C":
        result = (grade + 273.15)
    elif scale == "F":
        result = (grade - 32) * (5/9) + 273.15
    else:
        result = grade
    return result


def ConvertToFarenheit(grade, scale):
    if scale == "C":
        result = (grade * (9/5)) + 32
    elif scale == "K":
        result = (grade - 273.15) * (9/5) + 32
    else:
        result = grade
    return result

class TemperatureScale:
    Celsius = "C"
    Kelvin = "K"
    Farenheit = "F"

class Temperature:

    def __init__(self, Grade, Scale):
        self.grade = Grade
        self.scale = Scale

    def Sum(self,other):
        if self.scale == "C":
            GradeResult = ConvertToCelsius(other.grade, other.scale)
        elif self.scale == "K":
            GradeResult = ConvertToKelvin(other.grade, other.scale)
        elif self.scale == "F":
            GradeResult = ConvertToFarenheit(other.grade, other.scale)
        else:
            GradeResult = 0
        SumResult = self.grade + GradeResult
        return SumResult

    def Divide(self,other):
        if self.scale == "C":
            GradeResult = ConvertToCelsius(other.grade,other.scale)
        elif self.scale == "K":
            GradeResult = ConvertToKelvin(other.grade,other.scale)
        elif self.scale == "F":
            GradeResult = ConvertToFarenheit(other.grade,other.scale)
        else:
            GradeResult = 0
        DivideResult = self.grade / GradeResult
        return  DivideResult

    def Substract(self,other):
        if self.scale == "C":
            GradeResult = ConvertToCelsius(other.grade,other.scale)
        elif self.scale =="K":
            GradeResult = ConvertToKelvin(other.grade,other.scale)
        elif self.scale == "F":
            GradeResult = ConvertToFarenheit(other.grade,other.scale)
        else:
            GradeResult = 0
        SubResult = self.grade - GradeResult
        return SubResult

    def Multiply(self,other):
        if self.scale =="C":
            GradeResult = ConvertToCelsius(other.grade,other.scale)
        elif self.scale == "F":
            GradeResult = ConvertToFarenheit(other.grade,other.scale)
        elif self.scale == "K":
            GradeResult = ConvertToKelvin(other.grade,other.scale)
        else:
            GradeResult = 0
        MultiplyResult = self.grade * GradeResult
        return MultiplyResult

def Calculate(grade1,scale1,grade2,scale2,operacion):

    if (grade1 or grade2 != 0) and (grade1 or grade2 != ""):
          Temp1 = Temperature(grade1, scale1)
          Temp2 = Temperature(grade2, scale2)
          if operacion == 1: #Sum
              Temp3 = round(Temperature.Sum(Temp1, Temp2), 2)
          elif operacion == 2: #Substract
              Temp3 = round(Temperature.Substract(Temp1, Temp2), 2)
          elif operacion == 3: #Divide
              Temp3 = round(Temperature.Divide(Temp1, Temp2), 2)
          elif operacion == 4: #Multiply
              Temp3 = round(Temperature.Multiply(Temp1, Temp2))
          else:
               Temp3 = "Operacion Invalida"
    elif not grade1 or grade2:
        Temp3 = "Vacio"
    else:
        Temp3 = "Invalido"
    return Temp3

if __name__ == '__main__':
    result = Calculate(3, TemperatureScale.Celsius, 275.15, TemperatureScale.Kelvin, 4)
    print(result)



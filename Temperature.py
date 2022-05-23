
def ConvertToCelsius(grade, scale):
    if scale == "F":
        GradeResult = (grade - 32) * (5/9)
    elif scale == "K":
        GradeResult = grade - 273.15
    else:
        GradeResult = grade

    return GradeResult
def ConvertToFarenheit(grade,scale):

    if scale == "C":
        GradeResult = (grade * (9/5)) + 32
    elif scale == "K":
        GradeResult = (grade - 273.15) * (9/5) + 32
    else:
        GradeResult = grade
    return GradeResult

def ConvertToKelvin(grade,scale):
    if scale == "C":
        GradeResult = grade + 273.15
    elif scale == "F":
        GradeResult = (grade - 32) * (5/9) + 273.15
    else:
        GradeResult = grade

    return GradeResult

class Temperature:

    def __init__(self, Grade, Scale):
        self.grade = Grade
        self.scale = Scale

    def Multiply(self, other):
        if self.scale == "C":
            GradeConverted = ConvertToCelsius(other.grade, other.scale)
            MultiplyResult = self.grade * GradeConverted
        elif self.scale == "K":
            GradeConverted = ConvertToKelvin(other.grade, other.scale)
            MultiplyResult = self.grade * GradeConverted
        elif self.scale == "F":
            GradeConverted = ConvertToFarenheit(other.grade, other.scale)
            MultiplyResult = self.grade * GradeConverted
        else:
            MultiplyResult = 0
        return round(MultiplyResult, 2)

    def subtract(self, other):
        if self.scale == "C":
            GradeConverted = ConvertToCelsius(other.grade, other.scale)
            SubtractResult = self.grade - GradeConverted
        elif self.scale == "K":
            GradeConverted = ConvertToKelvin(other.grade, other.scale)
            SubtractResult = self.grade - GradeConverted
        elif self.scale == "F":
            GradeConverted = ConvertToFarenheit(other.grade,other.scale)
            SubtractResult = self.grade - GradeConverted
        else:
            SubtractResult = 0

        return round(SubtractResult, 2)


    def __add__(self, other):

            if self.scale == "C":
                GradeConverted = ConvertToCelsius(other.grade, other.scale)
                SumResult = self.grade + GradeConverted

            elif self.scale == "K":
                GradeConverted = ConvertToKelvin(other.grade, other.scale)
                SumResult = self.grade+GradeConverted
            elif self.scale == "F":

                GradeConverted = ConvertToFarenheit(other.grade,other.scale)
                SumResult = self.grade+GradeConverted
            else:
                SumResult = 0

            return round(SumResult, 2)

    def Divide(self,other):
        if self.scale == "C":
            GradeConverted = ConvertToCelsius(other.grade, other.scale)
            DivideResult = self.grade/GradeConverted
        elif self.scale == "K":
            GradeConverted = ConvertToKelvin(other.grade, other.scale)
            DivideResult = self.grade/GradeConverted
        elif self.scale == "F":
            GradeConverted = ConvertToFarenheit(other.grade, other.scale)
            DivideResult = self.grade/GradeConverted
        else:
            DivideResult = 0
        return round(DivideResult, 2)
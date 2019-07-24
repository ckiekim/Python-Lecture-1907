import math
class Calc:
    def add(self, x, y):
        return x+y
    def sub(self, x, y):
        return x-y
    def mul(self, x, y):
        return x*y
    def div(self, x, y):
        return x/y

class EngCalc(Calc):
    def sin(self, x):
        return math.sin(x)
    def cos(self, x):
        return math.cos(x)
    def tan(self, x):
        return math.tan(x)

eng = EngCalc()
print(eng.add(10, 20))
print(eng.sin(2*math.pi))
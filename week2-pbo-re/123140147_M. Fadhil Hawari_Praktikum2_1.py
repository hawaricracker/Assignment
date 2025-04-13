import math

class calculator():
    def __init__(self, a):
        self.a = a
    
    def __add__(self, other):
        return calculator(self.a + other.a)
    
    def __mul__(self, other):
        return calculator(self.a * other.a)
    
    def __truediv__(self, other):
        if other.a == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return calculator(self.a / other.a)
    
    def __sub__(self, other):
        return calculator(self.a - other.a)
    
    def __log__(self, other):
        if other.a <= 0:
            raise ValueError("Logarithm base must be greater than zero.")
        return calculator(math.log(self.a))
    
    def __pow__(self, other):
        return calculator(self.a ** other.a)
    
    def __str__(self):
        return str(self.a)
    
calc1 = calculator(10)
calc2 = calculator(5)

print(calc1 + calc2)  # Output: 15
print(calc1 - calc2)  # Output: 5
print(calc1 * calc2)  # Output: 50
print(calc1 / calc2)  # Output: 2.0
print(calc1 ** calc2)  # Output: 100000
print(calc1.__log__(calc2))  # Output: 2.3

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, x):
        self.value += x

    def subtract(self, x):
        self.value -= x

    def multiply(self, x):
        self.value *= x

    def divide(self, x):
        if x != 0:
            self.value /= x

    def clear(self):
        self.value = 0

calc = Calculator()

calc.add(10)
print("Результат add(10):", calc.value)
calc.multiply(5)
print("Результат multiply(5):", calc.value)
calc.subtract(15)
print("Результат subtract(15):", calc.value)
calc.divide(5)
print("Результат divide(5):", calc.value)
calc.clear()
print("Результат clear():", calc.value)

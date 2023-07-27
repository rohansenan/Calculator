

class Calc:
    def __init__(self):
        self.history = []
        self.n1 = self.history[-1] if self.history else 0
        self.n2 = None
        self.decimal_pressed = False
        self.second_number_turn = False
        self.operator = ""



def multiplication(x, y):
    return x * y

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def division(x, y):
    if y == 0:
        return "Undefined"
    return x / y

def power(x, y):
    y = int(y)
    if y == 0:
        return 1
    n = x
    for i in range(y - 1):
        n *= x
    return n

def root(x, y):
    if y == 0:
        return "Undefined"
    n = 1
    for i in range(1000):
        n = n - ((power(n, y) - x) / (y * power(n, y - 1)))
    return n

operations = {
    "division" : division,
    "multiplication" : multiplication,
    "subtraction" : subtraction,
    "addition" : addition,
    "exponent" : power,
    "root" : root
}
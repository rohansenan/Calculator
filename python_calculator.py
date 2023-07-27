import os
os.system('cls' if os.name == 'nt' else 'clear')

from ast import Del
from ctypes import sizeof
from curses.ascii import isdigit
from lib2to3.pgen2.token import OP
from multiprocessing.sharedctypes import Value
from re import L

def multiplication(x, y):
    return x * y

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def division(x, y):
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
    n = 1
    for i in range(1000):
        n = n - ((power(n, y) - x) / (y * power(n, y - 1)))
    return n

operators = ["+", "-", "*", "/", "^", "c", "q", "d", "root"]

class OperatorError (Exception):
    pass

class DeleteError (Exception):
    pass

class NullHistory (Exception):
    pass

class Delete (Exception):
    pass

class DeleteOne (Exception):
    pass

class DivideZero (Exception):
    pass

print("Decimal roots and powers will be rounded down.")
print("To exit calculator input 'q', to clear all previous inputs input 'c', to delete preivious input, input 'd'")
print("Here are the supported operations: ")
print("Mulitplication: *")
print("Division: /")
print("Addition: +")
print("Subtraction -")
print("Exponent: ^")
print("Root: root")

while True:
    exit = False
    reset = False

    history = []

    def record(answer):
        history.append(answer)
        print("Answer:", answer)

    try:
        n1 = float(input ("input number: "))
    
    except ValueError:
        print("Please input a number.")
        reset = True

    while not reset:
        try:
            operator = input ("input operator: ")
            
            if operator not in operators:
                raise OperatorError
            
            if operator == "c":
                if history:
                    del history
                    break
                else:
                    raise NullHistory


            elif operator == "d":
                if history:
                    if len(history) == 1:
                        raise DeleteOne
                    else:
                        raise Delete
                else:
                    raise DeleteError

            elif operator == "q":
                exit = True
                break
            
            n2 = float(input ("input number: "))

            if history:
                n1 = history[len(history) - 1]

            if operator == "*":
                answer = multiplication(n1, n2)

            elif operator == "+":
                answer = addition(n1, n2)

            elif operator == "-":
                answer = subtraction(n1, n2)

            elif operator == "/":
                if n2 == 0:
                    raise DivideZero
                else:
                    answer = division(n1, n2)

            elif operator == "^":
                answer = power(n1, n2)

            elif operator == "root":
                answer = root(n1, n2)
            
            else:
                raise OperatorError

            record(answer)

        except ValueError:
            print("Please input a number.")

        except OperatorError:
            print("Invalid operator.")

        except DeleteError:
            print("Cannot delete further.")

        except NullHistory:
            print("History already clear.")

        except DeleteOne:
            break

        except Delete:
            del history[-1]
            print (history[-1])

        except DivideZero:
            print ("Cannot divide by zero.")
            
    if exit == True:
        break
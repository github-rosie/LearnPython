# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operation: str, a: float, b: float):
    if operation == 'add':
        return add(a, b)
    elif operation == 'subtract':
        return subtract(a, b)
    else:
        raise ValueError("Unknown operation")

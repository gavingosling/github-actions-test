"""
This is a simple calculation module. It contains addition, subtraction, maximum,, minimum, multiplication and divison.
"""

def add(a, b):
    """
    Adds two numbers.
    >>> add(3, 2)
    5
    """

    return a + b


def subtract(a, b):
    """
    Subtracts two numbers.
    >>> subtract(3, 2)
    1
    >>> subtract(2, 3)
    -1
    """

    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.
    >>> multiply(3, 2)
    6
    """

    return a * b


def divide(a, b):
    """
    Divides two numbers.
    Automatically raises ZeroDivisionError.
    >>> divide(3.0, 2.0)
    1.5
    >>> divide(1.0, 0)
    Traceback (most recent call last):
        …
    ZeroDivisionError: float division by zero
    """

    return a * 1.0 / b


def maximum(a, b):
    """
    Finds the maximum of two numbers.
    >>> maximum(3, 2)
    3
    >>> maximum(2, 3)
    3
    >>> maximum(3, 3)
    3
    """

    return a if a >= b else b


def minimum(a, b):
    """
    Finds the minimum of two numbers.
    >>> minimum(3, 2)
    2
    >>> minimum(2, 3)
    2
    >>> minimum(2, 2)
    2
    """

    return a if a <= b else b
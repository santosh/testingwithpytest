"""
This module defines multiply(a, b) and divide(a, b).
>>> import unnecessary_math as um

Here's how you use multiply:
>>> um.multiply(3, 4)
12
>>> um.multiply('a', 3)
'aaa'

Here is howy you use divide:
>>> um.divide(10, 5)
2.0
"""


def multiply(a, b):
    """Returns a multiplied by b.
    >>> import unnecessary_math as um
    >>> um.multiply(3, 4)
    12
    >>> um.multiply('a', 3)
    'aaa'
    """
    return a * b


def divide(a, b):
    """
    Returns a divided by b.
    >>> import unnecessary_math as um
    >>> um.divide(10, 5)
    2.0
    """
    return a / b

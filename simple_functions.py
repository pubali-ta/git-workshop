# Custom python functions

def double_number(a):
    """
    Returns the input number multiplied by 2.

    Args:
        a (int or float): The number to be doubled.

    Returns:
        int or float: The result of doubling the input number.
        
    Examples:
        >>> double_number(5)
        10
        >>> double_number(3.5)
        7.0
    """
    
    print(f'value before double_number(): {a}')
    b = a+a
    print(f'value after double_number(): {b}')
    return b


def square_number(a):
    """

    Returns the square of the input number.

    Args:
        a (int or float): The number to be squared.

    Returns:
        int or float: The square of the input number (a²).

    Examples:
        >>> square_number(4)
        16
        >>> square_number(2.5)
        6.25
    """
    print(f'value before square_number(): {a}')
    b = a*a
    print(f'value after square_number(): {b}')
    return b

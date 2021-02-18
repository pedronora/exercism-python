def square(number):
    if 1 > number or number > 64:
        raise ValueError('The total number of squares on the chessboard is 64, starting from 1 to 64, inclusive.')
    return 2**(number - 1)


def total():
    return 2**64 - 1

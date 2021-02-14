def is_armstrong_number(number):
    sum_of_powers = sum(int(n)**len(str(number)) for n in str(number))
    return number == sum_of_powers

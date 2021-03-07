def factors(value):
    factors_list = []
    # Divisible by 2:
    while value % 2 == 0:
            factors_list.append(2)
            value = value / 2

    # Divisible by other primes numbers:
    sqrt = int(value**0.5)
    for i in range(3, sqrt + 1, 2):
        while value % i == 0:
            factors_list.append(i)
            value = value / i

    # If value is prime
    if value > 2:
        factors_list.append(value)

    return factors_list

def classify(number):
    if number <= 0:
        raise ValueError('Number must be positive')

    divisors = sum(n for n in range(1, number // 2 + 1) if number % n == 0)
    
    if divisors == number:
        return 'perfect'
    elif divisors > number:
        return 'abundant'
    else:
        return 'deficient'

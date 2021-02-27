def classify(number):
    if number <= 0:
        raise ValueError('Number must be positive')

    aliquot_sum = sum(n for n in range(1, number // 2 + 1) if number % n == 0)
    
    if aliquot_sum == number:
        return 'perfect'
    elif aliquot_sum > number:
        return 'abundant'
    else:
        return 'deficient'

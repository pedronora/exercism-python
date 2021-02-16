def prime(number):
    if number == 0:
        raise ValueError('Number must bigger than zero')
    primes = [2]
    n = 3
    while len(primes) < number:
        for prime in primes:
            if n % prime == 0:
                break
        else:
            primes.append(n)
        n += 2

    return primes[-1]

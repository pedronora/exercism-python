def sum_of_multiples(limit, multiples):
    mult = set()
    for n in multiples:
        if n != 0:
            for x in range(limit):
                if x % n == 0:
                    mult.add(x)
    return sum(mult)

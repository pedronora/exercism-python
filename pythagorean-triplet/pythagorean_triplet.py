def triplets_with_sum(number):
    # c² = a² + b² ==> c = (a² + b²)**(1/2)
    triangle = []
    for b in range(number // 3):
        for a in range(b + 1, number // 2):
            c = (a**2 + b**2)**(1/2)
            if c % 1 == 0 and (a + b + c) == number:
                triangle.append(sorted([a, b, int(c)]))
    return sorted(triangle)

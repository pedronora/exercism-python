def largest_product(series, size):
    if size < 0:
        raise ValueError('size must be positive')
    all_products = []
    n = 0
    while (n + size) <= len(series):
        product = 1
        for i in series[n: n + size]:
            product *= int(i)
        all_products.append(product)
        n += 1
    return max(all_products)

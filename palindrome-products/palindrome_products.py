# def largest(min_factor, max_factor):
#     if max_factor < min_factor:
#         raise ValueError('max_factor must be greater than min_factor')

#     max_palindrome = min_factor**2
#     for x in range(max_factor, min_factor, -1):
#         for y in range(x, min_factor, -1):
#             product = x * y
#             if product > max_palindrome:
#                 if str(product) == str(product)[::-1]:
#                     max_palindrome = product

#     factors = []
#     for x in range(min_factor, max_factor+1):
#         for y in range(min_factor, max_factor+1):
#             if x*y == max_palindrome:
#                 if sorted([x, y]) not in factors:
#                     factors.append(sorted([x, y]))
#     if max_palindrome == min_factor**2:
#         return((None, []))
#     return (max_palindrome, factors)


# def smallest(min_factor, max_factor):
#     if max_factor < min_factor:
#         raise ValueError('min_factor must be greater than max_factor')

#     min_palindrome = max_factor**2
#     for x in range(min_factor, max_factor):
#         for y in range(x, max_factor):
#             product = x * y
#             if product < min_palindrome:
#                 if str(product) == str(product)[::-1]:
#                     min_palindrome = product
  
#     factors = []
#     for x in range(min_factor, max_factor):
#         for y in range(min_factor, max_factor):
#             if x*y == min_palindrome:
#                 if sorted([x, y]) not in factors:
#                     factors.append(sorted([x, y]))

#     if min_palindrome == max_factor**2:
#         return ((None, []))
#     return (min_palindrome, factors)

# ================================================================ test session starts ================================================================
# platform linux -- Python 3.8.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
# rootdir: /home/user/Documents/.../exercism/python/palindrome-products
# collected 12 items                                                                                                                                  

# palindrome_products_test.py ............                                                                                                      [100%]

# ================================================================ 12 passed in 17.38s ================================================================


# bidouille's solution
# https://exercism.io/tracks/python/exercises/palindrome-products/solutions/f9f2f06a697b44359d3fa789e90d9451
def smallest(min_factor, max_factor):
    return extreme(min_factor, max_factor)


def largest(min_factor, max_factor):
    return extreme(min_factor, max_factor, step=-1)


def extreme(mini, maxi, step=1):
    if maxi < mini:
        raise ValueError("Unordered factors")
    for total in range(2 * mini, 2 * maxi + 1)[::step]:
        start, stop = ((total + 1) // 2, maxi) if step < 0 else (mini, total // 2)
        for a in range(start, stop + 1):
            number = a * (total - a)
            if is_palindrome(number):
                a, b = (a, total - a)[::step]
                factors = [[k, number // k] for k in range(a, b + 1) if number % k == 0]
                return number, factors
    return None, []


def is_palindrome(number):
    stg = str(number)
    return stg == stg[::-1]

# ================================================================ test session starts ================================================================
# platform linux -- Python 3.8.6, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
# rootdir: /home/user/Documents/.../exercism/python/palindrome-products
# collected 12 items                                                                                                                                  

# palindrome_products_test.py ............                                                                                                      [100%]

# ================================================================ 12 passed in 0.05s =================================================================

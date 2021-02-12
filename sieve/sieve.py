def primes(limit):
    all_numbers = list(range(2, limit + 1))
    for n in range(2, limit + 1):
        for num in range(n+1, limit + 1):
            if num % n == 0 and num in all_numbers:
                all_numbers.remove(num)                
    return all_numbers

# davidjoeressen's solution at 
# https://exercism.io/tracks/python/exercises/sieve/solutions/0895a76d4f96486ea021d9f752f6d490

# def primes(limit):
#     candidates = list(range(2,limit+1))
#     result = []
#     while len(candidates) > 0:
#         n = candidates[0]
#         result.append(n)
#         for m in range(n,limit+1,n):
#             if m in candidates:
#                 candidates.remove(m)
#     return result

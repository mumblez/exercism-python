def prime_factors(num):
    result = []
    factor=2
    while factor <= num:
        if num%factor == 0:
            result.append(factor)
            num = num // factor
        else:
            factor += 1
    return result

def sum_of_multiples(limit, nums):
    return sum(set(x for n in nums for x in range(n, limit, n)))

def sum_of_multiples(limit, nums):
    multiples = [x for x in range(1, limit) for y in nums if x%y == 0]
    return sum(set(multiples))

import math

def sieve(limit):
    if limit == 1: return []
    if limit == 2: return [2]

    # we can cut out all the even numbers
    numList = list(range(3, limit+1, 2))
    # and put 2 back in
    numList.insert(0, 2)

    for n in range(3, math.floor(math.sqrt(limit))+1):
        for multiplier in range(2, (limit//2 + 1)):
            num = n*multiplier
            if num > limit:
                break
            if num in numList:
                numList.remove(num)
    return numList

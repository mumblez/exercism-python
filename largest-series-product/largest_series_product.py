from functools import reduce

def largest_product(numString, span):
    if span == 0: return 1
    if len(numString) < 1: raise ValueError("empty string")
    if span > len(numString): raise ValueError("span larger then number of digits")
    if span < 0: raise ValueError("Negative span")
    if any(not x.isdigit() for x in numString): raise ValueError("Invalid character")

    highestValue = 0
    for i in range(len(numString)-span+1):
        currentValue = reduce(lambda x,y: x*y, [int(x) for x in list(numString[i:i+span])])
        if currentValue > highestValue:
            highestValue = currentValue

    return highestValue

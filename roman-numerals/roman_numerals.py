ator = {
    1: {"fiveN": "V", "oneN": "I"},
    10: {"fiveN": "L", "oneN": "X"},
    100: {"fiveN": "D", "oneN": "C"},
    1000: {"fiveN": "M", "oneN": "M"},
}

def numeral(year):
    if year > 3999 or year < 1:
        raise ValueError("Invalid Year")

    res = ''

    for yearUnit in [1000, 100, 10, 1]:
        unit = year // yearUnit
        if unit < 1:
            continue

        if unit in [1, 2, 3]:
            res += ator[yearUnit]['oneN'] * unit
        elif unit in [5,6,7,8]:
            res += ator[yearUnit]['fiveN']
            res += ator[yearUnit]['oneN'] * (unit - 5)
        elif unit == 4:
            res += ator[yearUnit]['oneN']
            res += ator[yearUnit]['fiveN']
        elif unit == 9:
            res += ator[yearUnit]['oneN']
            res += ator[yearUnit*10]['oneN']

        year -= (yearUnit * unit)

    return res

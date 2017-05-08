real = dict(zip(range(1,10), 'one two three four five six seven eight nine'.split()))
tens = dict(zip(range(2,10), 'twenty thirty forty fifty sixty seventy eighty ninety'.split()))
teens = dict(zip(range(10,20), 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()))
big = 'thousand million billion trillion quadrillion quintillion'.split()

def section(num):
    unit = num % 10
    ten = (num // 10) % 10
    hundred = (num // 100) % 10
    res = ''

    if hundred > 0: res += str(real[hundred]) + ' hundred'
    if unit == 0 and ten == 0: return res
    if (unit > 0 or ten > 0) and hundred > 0: res += ' and '
    if ten > 1:
        res += tens[ten]
    if ten == 1:
        res += teens[10 + unit]
        return res
    if unit == 0: return res
    if ten > 1 and unit > 0: res += '-'
    res += real[unit]
    return res


def say(num):
    res = ''
    if num == 0: return 'zero'
    if num < 0 or num == 1e12:
        raise AttributeError

    numSections = []

    while num > 0:
        numSections.append(num % 1000)
        num = num // 1000

    numSections.reverse()

    bigSection = len(numSections) -2
    for idx, ns in enumerate(numSections):
        res += section(ns)
        if idx + 1 < len(numSections):
            if numSections[idx] == 0 and numSections[idx+1] < 100 and numSections[idx+1] > 0:
                res += ' and '
        if bigSection >= 0 and ns > 0:
            res += ' ' + big[bigSection] + ' '
        bigSection -= 1

    return res.replace('  ', ' ').strip()

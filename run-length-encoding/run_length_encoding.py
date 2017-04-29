def process(qty, char):
    if qty == 1:
        return char
    return str(qty)+char


def decode(string):
    result = ''
    digitString = ''
    for c in string:
        if c.isdigit():
            digitString += c
        else:
            if len(digitString) > 0:
                result += c * int(digitString)
                digitString = ''
            else:
                result += c
    return result

def encode(string):
    counter = 1
    lastChar = ''
    result = ''

    for c in enumerate(list(string)):
        if c[0] == 0:
            lastChar = c[1]
        elif c[1] == lastChar:
            counter += 1
        else:
            result += process(counter, lastChar)
            counter = 1
            lastChar = c[1]

        if c[0] == len(string)-1:
            result += process(counter, lastChar)
    return result

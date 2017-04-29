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

# a better solution - http://exercism.io/submissions/fb280fc95a4d4cf4a925e2904fe225e6
# regex to split and filter string and string slicing
# groupby from itertools looks very useful

# import re
# from itertools import groupby
#
# def decode(string):
#     sequence = re.split("(\d+[A-Za-z]{1}|[A-Za-z]{1})", string)
#     sequence = list(filter(None, sequence))
#     decoded = ""
#     for code in sequence:
#         if len(code) == 1:
#             decoded += code
#         else:
#             decoded += int(code[:-1])*code[-1]
#     return decoded
#
# def encode(string):
#     split = ["".join(j) for k,j in groupby(string)]
#     encoded_str = ""
#     for chars in split:
#         if len(chars) == 1:
#             encoded_str += chars[0]
#         else:
#             encoded_str += "{}{}".format(len(chars),chars[0])
#     return encoded_str

from re import findall

responseMap = {
    'statement': 'Whatever.',
    'shouting': 'Whoa, chill out!',
    'question': 'Sure.',
    'silence': 'Fine. Be that way!'
}

def hey(s):
    s = findall(r'[a-zA-Z0-9?]*', s)
    s = ''.join(s)

    if len(s) == 0:
        return responseMap['silence']

    shouting = True
    for c in s:
        if c.isalpha() and c.islower():
            shouting = False
            break
    if shouting and any(c.isalpha() for c in s):
        return responseMap['shouting']

    if s.endswith('?'):
        return responseMap['question']

    return responseMap['statement']

# far simpler solution - http://exercism.io/submissions/5d27964da5f14b62ba66b60bb23fcaeb
# def hey(said):
#     "this is Bob's brain"
#     salute = said.strip()
#     if salute == "":
#         return "Fine. Be that way!"
#     elif salute.isupper():
#         return "Whoa, chill out!"
#     elif salute[-1] == "?":
#         return "Sure."
#     else:
#         return "Whatever."

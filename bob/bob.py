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

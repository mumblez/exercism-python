def is_isogram(s):
    d = dict()
    for c in s.lower():
        if c.isalpha():
            if c in d:
                return False
            d[c] = True
        else:
            continue
    return True

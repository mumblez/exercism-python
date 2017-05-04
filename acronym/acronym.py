def abbreviate(sentence):
    words = sentence.replace('-', ' ').split()
    acm = ''
    for word in words:
        for idx, letter in enumerate(list(word)):
            if idx == 0:
                acm += letter
            elif letter.isupper() and word[idx-1].islower():
                acm += letter
    return acm.upper()

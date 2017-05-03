def abbreviate(sentence):
    words = sentence.replace('-', ' ').split()
    acm = ''
    for word in words:
        for i in range(len(word)):
            if i == 0:
                acm += word[i].upper()
            elif word[i].isupper() and word[i-1].islower():
                acm += word[i].upper()
    return acm

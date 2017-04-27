def is_pangram(sentence):
    return len(set(c.lower() for c in sentence if c.isalpha())) == 26

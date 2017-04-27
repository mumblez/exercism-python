from re import findall
from collections import Counter

def word_count(s):
    words = findall('[a-z0-9]+', s.lower())
    return dict(Counter(words))

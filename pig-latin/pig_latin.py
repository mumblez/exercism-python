vowels = list('aeiou')

def encode(word):
    vowelIndex = 0
    for k, v in enumerate(word):
        if v in vowels:
            # exception for 'u'
            if v == 'u' and word[k+1] in vowels:
                vowelIndex += 1
            vowelIndex += k
            break
    # exeption for xray (wtf)
    if vowelIndex == 0 or vowelIndex > 3 or word[len(word)-2:] == 'ay':
        return word + 'ay'
    # from first encountered vowel, put constonant at end with 'ay'
    return word[vowelIndex:] + word[:vowelIndex] + 'ay'

def translate(sentence):
    words = sentence.split()
    res = []
    for word in words:
        res.append(encode(word))
    return ' '.join(res)

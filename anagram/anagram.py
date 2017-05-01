def detect_anagrams(word, candidates):
    return [w for w in candidates if w.lower() != word.lower() and ''.join(sorted(w.lower())) == ''.join(sorted(word.lower()))]

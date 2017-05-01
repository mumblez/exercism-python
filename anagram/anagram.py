def detect_anagrams(word, candidates):
    return [w for w in candidates if w.lower() != word.lower() and sorted(w.lower()) == sorted(word.lower())]

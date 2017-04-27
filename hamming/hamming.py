def distance(s1, s2):
    if len(s1) != len(s2): raise ValueError
    return len([k for k, v in zip(s1, s2) if k != v])

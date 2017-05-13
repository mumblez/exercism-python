def transform(legacy_data):
    return {letter.lower(): value for value, letterList in legacy_data.items() for letter in letterList}

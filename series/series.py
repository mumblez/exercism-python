def slices(sequence, length):
    if len(sequence) < length or length == 0:
        raise ValueError

    results = []

    for i in range(len(sequence)-length+1):
        results.append([int(n) for n in list(sequence[i:i+length])])

    return results


def to_rna(sequence):
    DNA='GCTA'
    RNA='CGAU'
    if any(s for s in sequence if s not in DNA):
        return ''
    return sequence.translate(str.maketrans(DNA, RNA))

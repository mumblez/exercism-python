def to_rna(sequence):
    DNA='GCTA'
    RNA='CGAU'
    if len([s for s in sequence if s not in DNA]) > 0:
        return ''
    return sequence.translate(str.maketrans(DNA, RNA))

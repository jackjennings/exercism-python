COUNTERPARTS = {"A": "U", "C": "G", "G": "C", "T": "A"}


def to_rna(dna_strand):
    return "".join(COUNTERPARTS[n] for n in list(dna_strand))

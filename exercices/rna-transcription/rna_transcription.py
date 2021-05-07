def to_rna(dna_strand):
    return str.translate(dna_strand, str.maketrans('GCTA', 'CGAU'))

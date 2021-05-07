CODON_TABLE = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": "STOP",
        "UAG": "STOP",
        "UGA": "STOP"
}


def _to_codons(strand) -> list[str]:
    return [strand[i:i + 3].upper() for i in range(0, len(strand), 3)]


def proteins(strand):
    protein_lst: list[str] = []

    for codon in _to_codons(strand):
        if (protein := CODON_TABLE[codon]) != CODON_TABLE['UAA']:
            protein_lst.append(protein)
        else:
            break

    return protein_lst

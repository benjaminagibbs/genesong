''' list possible codons for any combination of 3 nucleotides '''

codon_ref = {
    'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L'
    'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S'
    'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*'
    'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W'
    'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L'
    'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P'
    'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q'
    'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R'
    'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M'
    'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T'
} # TODO: check copilot for errors
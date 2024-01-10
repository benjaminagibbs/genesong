from static.reference.codons import codon_ref
from static.reference.notes import note_ref

def sequence_to_notes(sequence, scale):
    codons = sequence_to_codons(sequence)
    notes = codons_to_notes(codons, scale)
    return notes


def sequence_to_codons(sequence):
    """Converts a string of nucleotides represented by a c t or g to a sequence of codons"""
    raw_codon = []
    codons = []
    for nucleotide in sequence:
        if nucleotide not in ['a', 'c', 't', 'g']:
            raise ValueError("Invalid nucleotide: {}".format(nucleotide))
    for i in range(0, len(sequence), 3):
        next = sequence[i:i+3]
        # map to codon_ref
        codons.append(codon_ref[next])
        # TODO: length handling
    return codons

def codons_to_notes(codons, scale : str):
    """Converts a sequence of codons to a sequence of notes"""
    # use static.reference.notes scale with same name as user input scale string
    # TODO: scale handling
    notes = []
    for i in codons:
        note = note_ref[i]
        notes.append(note)
    return notes
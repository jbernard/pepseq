# -*- coding: utf-8 -*-


class AminoAcid(object):

    """ Amino acids are molecules containing an amine group, a carboxylic acid
        group and a side chain that varies between different amino acids. """

    aminoAcids = {'G': ('Glycine',       'Gly', 57.05),
                  'A': ('Alanine',       'Ala', 71.09),
                  'S': ('Serine',        'Ser', 87.08),
                  'T': ('Threonine',     'Thr', 101.11),
                  'C': ('Cysteine',      'Cys', 103.15),
                  'V': ('Valine',        'Val', 99.14),
                  'L': ('Leucine',       'Leu', 113.16),
                  'I': ('Isoleucine',    'Ile', 113.16),
                  'M': ('Methionine',    'Met', 131.19),
                  'P': ('Proline',       'Pro', 97.12),
                  'F': ('Phenylalanine', 'Phe', 147.18),
                  'Y': ('Tyrosine',      'Tyr', 163.18),
                  'W': ('Tryptophan',    'Trp', 186.21),
                  'D': ('Aspartic Acid', 'Asp', 115.09),
                  'E': ('Glutamic Acid', 'Glu', 129.12),
                  'N': ('Asparagine',    'Asn', 114.11),
                  'Q': ('Glutamine',     'Gln', 128.14),
                  'H': ('Histidine',     'His', 137.14),
                  'K': ('Lysine',        'Lys', 128.17),
                  'R': ('Arginine',      'Arg', 156.19)}

    def __init__(self, letter):
        self.letter = letter.upper()
        self.name = AminoAcid.aminoAcids[self.letter][0]
        self.triple = AminoAcid.aminoAcids[self.letter][1]
        self.weight = AminoAcid.aminoAcids[self.letter][2]

    def __str__(self):
        return "%s (%s, %s) MW: %.2f" % (
                self.name, self.triple, self.letter, self.weight)


class Peptide(object):

    def __init__(self, amino_acids):
        self.weight = 0
        self.string = ""
        self.amino_acids = amino_acids
        for amino_acid in self.amino_acids:
            self.weight += amino_acid.weight
            self.string += ('%s' % (amino_acid.letter.lower()))
            if amino_acid is not self.amino_acids[-1]:
                self.string += ','

    def __cmp__(self, other):
        return cmp(self.weight, other.weight)

    def __str__(self):
        return "%d: %s" % (self.weight, self.string)

if __name__ == '__main__':

    import itertools

    fragment = (
            ((AminoAcid('a'), AminoAcid('t'), AminoAcid('k'))),
            ((AminoAcid('r'), AminoAcid('q'), AminoAcid('h'))),
            ((AminoAcid('r'), AminoAcid('q'), AminoAcid('h'))),
            ((AminoAcid('r'), AminoAcid('q'), AminoAcid('h'))),
            ((AminoAcid('r'), AminoAcid('q'), AminoAcid('h'))),
    )

    peptides = []
    sequences = tuple(itertools.product(*fragment))
    for sequence in sequences:
        peptides.append(Peptide(sequence))

    peptides.sort()
    for peptide in peptides:
        print peptide

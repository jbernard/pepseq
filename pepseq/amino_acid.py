# -*- coding: utf-8 -*-


class AminoAcid(object):

    """ Amino acids are molecules containing an amine group, a carboxylic acid
        group and a side chain that varies between different amino acids. """

    aminoAcids = {'G': ('Glycine',                  'Gly', 57.05),
                  'A': ('Alanine',                  'Ala', 71.09),
                  'S': ('Serine',                   'Ser', 87.08),
                  'T': ('Threonine',                'Thr', 101.11),
                  'C': ('Cysteine',                 'Cys', 103.15),
                  'V': ('Valine',                   'Val', 99.14),
                  'L': ('Leucine',                  'Leu', 113.16),
                  'I': ('Isoleucine',               'Ile', 113.16),
                  'M': ('Methionine',               'Met', 131.19),
                  'P': ('Proline',                  'Pro', 97.12),
                  'F': ('Phenylalanine',            'Phe', 147.18),
                  'Y': ('Tyrosine',                 'Tyr', 163.18),
                  'W': ('Tryptophan',               'Trp', 186.21),
                  'D': ('Aspartic Acid',            'Asp', 115.09),
                  'E': ('Glutamic Acid',            'Glu', 129.12),
                  'N': ('Asparagine',               'Asn', 114.11),
                  'Q': ('Glutamine',                'Gln', 128.14),
                  'H': ('Histidine',                'His', 137.14),
                  'K': ('Lysine',                   'Lys', 128.17),
                  'R': ('Arginine',                 'Arg', 156.19),
                  'B': ('Borono Phenylalanine',     'Bpa', 309.08),
    }

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
        self.amino_acids = amino_acids
        self.weight = 0
        self.string = ""
        for amino_acid in amino_acids:
            self.weight += amino_acid.weight
            self.string += ('%s' % (amino_acid.letter))

    def branch_before(self, index):
        self.weight = 0
        for (counter, amino_acid) in enumerate(self.amino_acids):
            if counter < index:
                self.weight += 2 * amino_acid.weight
            else:
                self.weight += amino_acid.weight
        self.string = '(' + self.string[0:index] + ')2' + self.string[index:]

    def __cmp__(self, other):
        return cmp(self.weight, other.weight)

    def __str__(self):
        return self.string


if __name__ == '__main__':

    import itertools

    LOW  = 2636.0
    HIGH = 2637.0

    possibilities = (
            (AminoAcid('B'), AminoAcid('Q'), AminoAcid('T'), AminoAcid('Y')),
            (AminoAcid('B'), AminoAcid('E'), AminoAcid('L'), AminoAcid('F')),
            (AminoAcid('B'), AminoAcid('D'), AminoAcid('S'), AminoAcid('H')),
            (AminoAcid('B'), AminoAcid('N'), AminoAcid('A'), AminoAcid('W')),
            (AminoAcid('K'), AminoAcid('N')),
            (AminoAcid('S'), AminoAcid('N'), AminoAcid('T'), AminoAcid('F')),
            (AminoAcid('T'), AminoAcid('D'), AminoAcid('G'), AminoAcid('W')),
            (AminoAcid('B'), AminoAcid('Q'), AminoAcid('P'), AminoAcid('H')),
            (AminoAcid('L'), AminoAcid('E'), AminoAcid('A'), AminoAcid('Y')),
    )

    peptides = []
    sequences = tuple(itertools.product(*possibilities))
    for sequence in sequences:
        if sequence[4].letter == 'K':
            peptide = Peptide(sequence)
            peptide.branch_before(4)
            peptides.append(peptide)

    peptides.sort()
    for peptide in peptides:
        if peptide.weight > LOW and peptide.weight < HIGH:
            print "%.2f %s" % (peptide.weight, peptide)

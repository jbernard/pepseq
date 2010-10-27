# -*- coding: utf-8 -*-

from amino_acid import AminoAcid
import unittest


class AminoAcidTestCase(unittest.TestCase):

    def test_glycine(self):
        amino_acid = AminoAcid('g')
        self.assertEqual(amino_acid.name, "Glycine")
        self.assertEqual(amino_acid.triple, "Gly")
        self.assertEqual(amino_acid.letter, "G")
        self.assertEqual(amino_acid.weight, 57.05)

    def test_alanine(self):
        amino_acid = AminoAcid('a')
        self.assertEqual(amino_acid.name, "Alanine")
        self.assertEqual(amino_acid.triple, "Ala")
        self.assertEqual(amino_acid.letter, "A")
        self.assertEqual(amino_acid.weight, 71.09)

    def test_serine(self):
        amino_acid = AminoAcid('s')
        self.assertEqual(amino_acid.name, "Serine")
        self.assertEqual(amino_acid.triple, "Ser")
        self.assertEqual(amino_acid.letter, "S")
        self.assertEqual(amino_acid.weight, 87.08)

    def test_threonine(self):
        amino_acid = AminoAcid('t')
        self.assertEqual(amino_acid.name, "Threonine")
        self.assertEqual(amino_acid.triple, "Thr")
        self.assertEqual(amino_acid.letter, "T")
        self.assertEqual(amino_acid.weight, 101.11)

    def test_cysteine(self):
        amino_acid = AminoAcid('c')
        self.assertEqual(amino_acid.name, "Cysteine")
        self.assertEqual(amino_acid.triple, "Cys")
        self.assertEqual(amino_acid.letter, "C")
        self.assertEqual(amino_acid.weight, 103.15)

    def test_valine(self):
        amino_acid = AminoAcid('v')
        self.assertEqual(amino_acid.name, "Valine")
        self.assertEqual(amino_acid.triple, "Val")
        self.assertEqual(amino_acid.letter, "V")
        self.assertEqual(amino_acid.weight, 99.14)

    def test_leucine(self):
        amino_acid = AminoAcid('l')
        self.assertEqual(amino_acid.name, "Leucine")
        self.assertEqual(amino_acid.triple, "Leu")
        self.assertEqual(amino_acid.letter, "L")
        self.assertEqual(amino_acid.weight, 113.16)

    def test_isoleucine(self):
        amino_acid = AminoAcid('i')
        self.assertEqual(amino_acid.name, "Isoleucine")
        self.assertEqual(amino_acid.triple, "Ile")
        self.assertEqual(amino_acid.letter, "I")
        self.assertEqual(amino_acid.weight, 113.16)

    def test_methionine(self):
        amino_acid = AminoAcid('m')
        self.assertEqual(amino_acid.name, "Methionine")
        self.assertEqual(amino_acid.triple, "Met")
        self.assertEqual(amino_acid.letter, "M")
        self.assertEqual(amino_acid.weight, 131.19)

    def test_proline(self):
        amino_acid = AminoAcid('p')
        self.assertEqual(amino_acid.name, "Proline")
        self.assertEqual(amino_acid.triple, "Pro")
        self.assertEqual(amino_acid.letter, "P")
        self.assertEqual(amino_acid.weight, 97.12)

    def test_phenylalanine(self):
        amino_acid = AminoAcid('f')
        self.assertEqual(amino_acid.name, "Phenylalanine")
        self.assertEqual(amino_acid.triple, "Phe")
        self.assertEqual(amino_acid.letter, "F")
        self.assertEqual(amino_acid.weight, 147.18)

    def test_tyrosine(self):
        amino_acid = AminoAcid('y')
        self.assertEqual(amino_acid.name, "Tyrosine")
        self.assertEqual(amino_acid.triple, "Tyr")
        self.assertEqual(amino_acid.letter, "Y")
        self.assertEqual(amino_acid.weight, 163.18)

    def test_tryptophan(self):
        amino_acid = AminoAcid('w')
        self.assertEqual(amino_acid.name, "Tryptophan")
        self.assertEqual(amino_acid.triple, "Trp")
        self.assertEqual(amino_acid.letter, "W")
        self.assertEqual(amino_acid.weight, 186.21)

    def test_aspartic_acid(self):
        amino_acid = AminoAcid('d')
        self.assertEqual(amino_acid.name, "Aspartic Acid")
        self.assertEqual(amino_acid.triple, "Asp")
        self.assertEqual(amino_acid.letter, "D")
        self.assertEqual(amino_acid.weight, 115.09)

    def test_glutamic_acid(self):
        amino_acid = AminoAcid('e')
        self.assertEqual(amino_acid.name, "Glutamic Acid")
        self.assertEqual(amino_acid.triple, "Glu")
        self.assertEqual(amino_acid.letter, "E")
        self.assertEqual(amino_acid.weight, 129.12)

    def test_asparagine(self):
        amino_acid = AminoAcid('n')
        self.assertEqual(amino_acid.name, "Asparagine")
        self.assertEqual(amino_acid.triple, "Asn")
        self.assertEqual(amino_acid.letter, "N")
        self.assertEqual(amino_acid.weight, 114.11)

    def test_glutamine(self):
        amino_acid = AminoAcid('q')
        self.assertEqual(amino_acid.name, "Glutamine")
        self.assertEqual(amino_acid.triple, "Gln")
        self.assertEqual(amino_acid.letter, "Q")
        self.assertEqual(amino_acid.weight, 128.14)

    def test_histidine(self):
        amino_acid = AminoAcid('h')
        self.assertEqual(amino_acid.name, "Histidine")
        self.assertEqual(amino_acid.triple, "His")
        self.assertEqual(amino_acid.letter, "H")
        self.assertEqual(amino_acid.weight, 137.14)

    def test_lysine(self):
        amino_acid = AminoAcid('k')
        self.assertEqual(amino_acid.name, "Lysine")
        self.assertEqual(amino_acid.triple, "Lys")
        self.assertEqual(amino_acid.letter, "K")
        self.assertEqual(amino_acid.weight, 128.17)

    def test_arginine(self):
        amino_acid = AminoAcid('r')
        self.assertEqual(amino_acid.name, "Arginine")
        self.assertEqual(amino_acid.triple, "Arg")
        self.assertEqual(amino_acid.letter, "R")
        self.assertEqual(amino_acid.weight, 156.19)

    def test_borono_phenylalanine(self):
        amino_acid = AminoAcid('b')
        self.assertEqual(amino_acid.name, "Borono Phenylalanine")
        self.assertEqual(amino_acid.triple, "Bpa")
        self.assertEqual(amino_acid.letter, "B")
        self.assertEqual(amino_acid.weight, 309.08)


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(AminoAcidTestCase)
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())

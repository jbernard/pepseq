# -*- coding: utf-8 -*-

import unittest


class PeptideTestCase(unittest.TestCase):
    pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PeptideTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

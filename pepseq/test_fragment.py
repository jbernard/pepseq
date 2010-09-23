# -*- coding: utf-8 -*-

import unittest


class FragmentTestCase(unittest.TestCase):
    pass

def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(FragmentTestCase)
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())

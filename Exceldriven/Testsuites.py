import sys
import unittest

from Exceldriven import test_mulitplewindow
from Exceldriven import test_assert


tc1 = unittest.TestLoader().loadTestsFromTestCase(test_mulitplewindow.test_multi)
tc2 = unittest.TestLoader().loadTestsFromTestCase(test_assert.test_hero1)
# tc1 = unittest.TestLoader().loadTestsFromTestCase(exceldata.test_hero)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(Asserttitle.test_hero1)
#
#
# smoke = unittest.TestSuite([tc1,tc2 ])
#
# runner = unittest.TextTestRunner(verbosity=2 ).run(smoke)
suite = unittest.TestSuite([tc2,tc1])
runner = unittest.TextTestRunner(verbosity=2).run(suite)

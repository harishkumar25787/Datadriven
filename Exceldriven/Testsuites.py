import sys
import unittest

from Exceldriven import multiplewindow
from Exceldriven import Asserttitle


tc1 = unittest.TestLoader().loadTestsFromTestCase(multiplewindow.test_multi)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Asserttitle.test_hero1)
# tc1 = unittest.TestLoader().loadTestsFromTestCase(exceldata.test_hero)
# tc2 = unittest.TestLoader().loadTestsFromTestCase(Asserttitle.test_hero1)
#
#
# smoke = unittest.TestSuite([tc1,tc2 ])
#
# runner = unittest.TextTestRunner(verbosity=2 ).run(smoke)
suite = unittest.TestSuite([tc2,tc1])
runner = unittest.TextTestRunner(verbosity=2).run(suite)

# if __name__ == '__main__':
#     unittest.runner

# -*- coding: utf-8 -*-
import doctest
import unittest

import trytond.tests.test_tryton
from trytond.tests.test_tryton import DB_NAME, doctest_setup, doctest_teardown

from tests.test_views_depends import TestViewsDepends


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestViewsDepends),
    ])
    if DB_NAME == ':memory:':
        test_suite.addTests(
            doctest.DocFileSuite(
                'scenario_stock_production_location.rst',
                setUp=doctest_setup,
                tearDown=doctest_teardown,
                encoding='utf-8',
                optionflags=doctest.REPORT_ONLY_FIRST_FAILURE
            )
        )
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())

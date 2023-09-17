
from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodel.PyutParameter import PyutParameter
from pyutmodel.PyutType import PyutType
from tests.TestBase import TestBase


class TestPyutParameter(TestBase):
    """
    """
    def setUp(self):
        super().setUp()

    def tearDown(self):
        pass

    def testFullString(self):
        pyutParameter: PyutParameter = PyutParameter(name='Ozzee', parameterType=PyutType('float'), defaultValue='1.0')

        expectedValue: str = 'Ozzee: float = 1.0'
        actualValue:   str = pyutParameter.__str__()

        self.assertEqual(expectedValue, actualValue, 'Full string representation has changed')

    def testNoDefaultValue(self):
        pyutParameter: PyutParameter = PyutParameter(name='Ozzee', parameterType=PyutType('float'))

        expectedValue: str = 'Ozzee: float'
        actualValue:   str = pyutParameter.__str__()

        self.assertEqual(expectedValue, actualValue, 'No default value string representation has changed')

    def testNoTypeOrDefaultValue(self):

        pyutParameter: PyutParameter = PyutParameter(name='Ozzee')

        expectedValue: str = 'Ozzee'
        actualValue:   str = pyutParameter.__str__()

        self.assertEqual(expectedValue, actualValue, 'No Type, no default value string representation has changed')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutParameter))

    return testSuite


if __name__ == '__main__':
    unitTestMain()

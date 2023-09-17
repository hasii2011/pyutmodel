
from typing import cast

from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodel.PyutStereotype import PyutStereotype
from tests.TestBase import TestBase


class TestPyutStereotype(TestBase):
    """
    """
    def setUp(self):
        super().setUp()

    def tearDown(self):
        pass

    def testBasic(self):
        pyutStereotype: PyutStereotype = PyutStereotype.toEnum(PyutStereotype.TYPE.value)

        self.assertEqual(PyutStereotype.TYPE, pyutStereotype, 'Basic conversion failing')

    def testBasicNoStereotype(self):
        pyutStereotype: PyutStereotype = PyutStereotype.toEnum(PyutStereotype.NO_STEREOTYPE.value)

        self.assertEqual(PyutStereotype.NO_STEREOTYPE, pyutStereotype, 'Basic conversion failing')

    def testBasicNoImplementationClass(self):
        pyutStereotype: PyutStereotype = PyutStereotype.toEnum(PyutStereotype.IMPLEMENTATION_CLASS.value)

        self.assertEqual(PyutStereotype.IMPLEMENTATION_CLASS, pyutStereotype, 'Basic conversion failing')

    def testEmptyString(self):
        pyutStereotype: PyutStereotype = PyutStereotype.toEnum('')

        self.assertEqual(PyutStereotype.NO_STEREOTYPE, pyutStereotype, 'Empty string conversion failing')

    def testNone(self):
        pyutStereotype: PyutStereotype = PyutStereotype.toEnum(cast(str, None))

        self.assertEqual(PyutStereotype.NO_STEREOTYPE, pyutStereotype, 'Empty string conversion failing')

    def testManySpaces(self):
        pyutStereotype: PyutStereotype = PyutStereotype.toEnum('    ')

        self.assertEqual(PyutStereotype.NO_STEREOTYPE, pyutStereotype, 'Empty string conversion failing')

def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutStereotype))

    return testSuite


if __name__ == '__main__':
    unitTestMain()

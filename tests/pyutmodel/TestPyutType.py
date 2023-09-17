
from typing import List

from unittest import main as unitTestMain
from unittest import TestSuite

from copy import deepcopy

from pyutmodel.PyutType import PyutType
from tests.TestBase import TestBase


class TestPyutType(TestBase):

    def setUp(self):
        super().setUp()
        self.strings = [
            "salut", "hello", "ca va ?"
        ]

    def testPyutTypeReadOnly(self):
        """Test PyutType class"""
        a: PyutType = PyutType("salut")
        b: PyutType = PyutType("s" + "alut")
        self.assertTrue(a.value == b.value)
        try:
            # noinspection PyUnresolvedReferences
            a.value = "Salut"
        except NotImplementedError as ae:
            self.logger.info(f'Expected error: {ae}')
            pass    # We should get this error
        else:
            self.fail("PyutType should not be modifiable by setName")

    def testDeepCopyPyutTypes(self):

        fieldTypes: List[str] = ['int', 'bool', 'float']
        originalTypes: List[PyutType] = []
        for x in range(len(fieldTypes)):
            aType: PyutType = PyutType(value=fieldTypes[x])
            originalTypes.append(aType)
        self.logger.info(f'originalTypes: {originalTypes}')

        doppleGangers: List[PyutType] = deepcopy(originalTypes)
        self.logger.info(f'doppleGangers: {doppleGangers}')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutType))

    return testSuite


if __name__ == '__main__':
    unitTestMain()

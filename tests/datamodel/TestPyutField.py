
from typing import cast
from typing import List

from logging import Logger
from logging import getLogger

from unittest import TestSuite
from unittest import main as unitTestMain

from copy import deepcopy

from pyutmodel.datamodel.PyutField import PyutField
from pyutmodel.datamodel.PyutType import PyutType
from pyutmodel.datamodel.PyutVisibilityEnum import PyutVisibilityEnum

from tests.TestBase import TestBase


class TestPyutField(TestBase):

    clsLogger: Logger = cast(Logger, None)

    fieldNames:        List[str]      = ['field1', 'field2', 'field3']
    fieldTypes:        List[PyutType] = [PyutType(value='int'),
                                         PyutType(value='bool'),
                                         PyutType(value='float')]
    fieldValues:       List[str]      = ['22', 'False', '62.34324']
    fieldVisibilities: List[PyutVisibilityEnum] = [PyutVisibilityEnum.PRIVATE,
                                                   PyutVisibilityEnum.PUBLIC,
                                                   PyutVisibilityEnum.PROTECTED]

    @classmethod
    def setUpClass(cls):
        TestBase.setUpLogging()
        TestPyutField.clsLogger = getLogger(__name__)

    def setUp(self):
        self.logger: Logger = TestPyutField.clsLogger

    def testDeepCopyList(self):

        originalFields: List[PyutField] = []
        for x in range(len(TestPyutField.fieldNames)):
            field: PyutField = PyutField(name=TestPyutField.fieldNames[x],
                                         fieldType=TestPyutField.fieldTypes[x],
                                         defaultValue=TestPyutField.fieldValues[x],
                                         visibility=TestPyutField.fieldVisibilities[x]
                                         )
            originalFields.append(field)
        self.logger.info(f'originalFields: {originalFields}')

        dopplegangers: List[PyutField] = deepcopy(originalFields)
        self.logger.info(f'{dopplegangers=}')

        for pyutField in dopplegangers:
            self.assertTrue(isinstance(pyutField.type, PyutType), 'Wrong type copied')
            self.assertTrue(isinstance(pyutField.visibility, PyutVisibilityEnum), 'Wrong visibility type copied')


def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()
    # noinspection PyUnresolvedReferences
    testSuite.addTest(unittest.makeSuite(TestPyutField))

    return testSuite


if __name__ == '__main__':
    unitTestMain()

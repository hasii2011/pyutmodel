
from typing import cast

from logging import Logger
from logging import getLogger

from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodel.PyutLink import PyutLink
from pyutmodel.PyutLinkType import PyutLinkType
from tests.TestBase import TestBase


class TestPyutLink(TestBase):
    """
    """
    clsLogger: Logger = cast(Logger, None)

    @classmethod
    def setUpClass(cls):
        TestBase.setUpLogging()
        TestPyutLink.clsLogger = getLogger(__name__)

        import warnings
        # To ignore this warning:
        # DeprecationWarning
        # Since this is legacy stuff;  May go away
        warnings.simplefilter("ignore", category=DeprecationWarning)

    def setUp(self):
        self.logger: Logger = TestPyutLink.clsLogger

    def tearDown(self):
        pass

    def testValidLinkType(self):

        pyutLink: PyutLink = PyutLink(name='ValidPyutLink')
        linkType: PyutLinkType = PyutLinkType.COMPOSITION

        pyutLink.linkType = linkType

        expectedLinkType: PyutLinkType = PyutLinkType.COMPOSITION
        actualLinkType:   PyutLinkType = pyutLink.linkType

        self.assertEqual(expectedLinkType, actualLinkType, 'Incorrect  valid legacy type support')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()
    # noinspection PyUnresolvedReferences
    testSuite.addTest(unittest.makeSuite(TestPyutLink))

    return testSuite


if __name__ == '__main__':
    unitTestMain()

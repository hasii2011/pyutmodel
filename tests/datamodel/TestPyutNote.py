
from typing import cast

from logging import Logger
from logging import getLogger

from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodel.PyutNote import PyutNote
from tests.TestBase import TestBase


class TestPyutNote(TestBase):
    """
    """
    clsLogger: Logger = cast(Logger, None)

    @classmethod
    def setUpClass(cls):
        TestBase.setUpLogging()
        TestPyutNote.clsLogger = getLogger(__name__)

    def setUp(self):
        self.logger: Logger = TestPyutNote.clsLogger

    def tearDown(self):
        pass

    def testDefaultNoteContent(self):
        """
        TODO:
        This test should be pulling the expectedContent from the plugin
        preferences file
        """

        expectedContent: str = 'Note text'

        pyutNote: PyutNote = PyutNote(noteText=expectedContent)

        expectedContent: str = 'Note text'
        actualContent:   str = pyutNote.content

        self.assertEqual(expectedContent, actualContent, 'Did not use preferences note content')

    def testNoneNoteContent(self):
        pyutNote: PyutNote = PyutNote(noteText=cast(str, None))

        expectedContent: str = cast(str, None)
        actualContent:   str = pyutNote.content

        self.assertEqual(expectedContent, actualContent, 'Did not use preferences note content')

    def testOurNoteContent(self):

        pyutNote: PyutNote = PyutNote(noteText='Humberto the Pythonista')

        expectedContent: str = 'Humberto the Pythonista'
        actualContent:   str = pyutNote.content

        self.assertEqual(expectedContent, actualContent, 'Did not use our note content')


def suite() -> TestSuite:
    """You need to change the name of the test class here also."""
    import unittest

    testSuite: TestSuite = TestSuite()
    # noinspection PyUnresolvedReferences
    testSuite.addTest(unittest.makeSuite(TestPyutNote))

    return testSuite


if __name__ == '__main__':
    unitTestMain()


from typing import cast

from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodel.PyutNote import PyutNote
from tests.TestBase import TestBase


class TestPyutNote(TestBase):
    """
    """
    def setUp(self):
        super().setUp()

    def tearDown(self):
        pass

    def testDefaultNoteContent(self):
        """
        TODO:
        This test should be pulling the expectedContent from the plugin
        preferences file
        """

        expectedContent: str      = 'Note text'
        pyutNote:        PyutNote = PyutNote(noteText=expectedContent)
        actualContent:   str      = pyutNote.content

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

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutNote))

    return testSuite


if __name__ == '__main__':
    unitTestMain()


from typing import cast

from logging import Logger
from logging import getLogger

from unittest import TestSuite
from unittest import main as unitTestMain

from pyutmodel.DisplayMethodParameters import DisplayMethodParameters
from pyutmodel.PyutMethod import PyutMethod
from pyutmodel.PyutMethod import PyutParameters
from pyutmodel.PyutMethod import SourceCode
from pyutmodel.PyutParameter import PyutParameter
from pyutmodel.PyutType import PyutType

from tests.TestBase import TestBase


class TestPyutMethod(TestBase):
    """
    """
    def setUp(self):
        super().setUp()
        self._pyutMethod: PyutMethod = PyutMethod(name='methodName')

    def tearDown(self):
        pass

    def testStringMethodWithParameters(self):

        pyutMethod: PyutMethod = self._pyutMethod

        PyutMethod.setStringMode(DisplayMethodParameters.WITH_PARAMETERS)

        self.assertEqual(DisplayMethodParameters.WITH_PARAMETERS, pyutMethod.getStringMode(), 'Did not get set correctly')

    def testStringMethodWithoutParameters(self):

        pyutMethod: PyutMethod = self._pyutMethod

        PyutMethod.setStringMode(DisplayMethodParameters.WITHOUT_PARAMETERS)

        self.assertEqual(DisplayMethodParameters.WITHOUT_PARAMETERS, pyutMethod.getStringMode(), 'Did not get set correctly')

    def testStringMethodWithParametersRepresentation(self):

        pyutMethod: PyutMethod = self._pyutMethod
        pyutMethod.returnType = PyutType('float')

        pyutMethod.parameters = self._makeParameters()
        PyutMethod.setStringMode(DisplayMethodParameters.WITH_PARAMETERS)

        defaultName: str = 'methodName'
        expectedRepresentation: str = f'+{defaultName}(intParam: int = 0, floatParam: float = 32.0): float'
        actualRepresentation:   str = pyutMethod.__str__()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Oops this does not match')

    def testStringMethodWithoutParametersRepresentation(self):

        pyutMethod:     PyutMethod = self._pyutMethod
        pyutMethod.returnType = PyutType('float')

        pyutMethod.parameters = self._makeParameters()
        PyutMethod.setStringMode(DisplayMethodParameters.WITHOUT_PARAMETERS)

        defaultName: str = 'methodName'
        expectedRepresentation: str = f'+{defaultName}(): float'
        actualRepresentation:   str = pyutMethod.__str__()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Oops this does not match')

    def testMethodSimpleParametersWithParameters(self):
        simpleMethod: PyutMethod = self._pyutMethod

        simpleMethod.parameters = self._makeSimpleParameters()
        PyutMethod.setStringMode(DisplayMethodParameters.WITH_PARAMETERS)

        defaultName: str = 'methodName'
        expectedRepresentation: str = (
            f'+{defaultName}('
            f'{simpleMethod.parameters[0].name}, '
            f'{simpleMethod.parameters[1].name}, '
            f'{simpleMethod.parameters[2].name}'
            ')'
        )
        actualRepresentation:   str = simpleMethod.__str__()

        self.assertEqual(expectedRepresentation, actualRepresentation, 'Simple Method Simple Parameters does not match')

    def testStashSourceCode(self):

        pyutMethod:        PyutMethod = self._generateAMethod()
        expectedLineCount: int = 5
        actualLineCount:   int = len(pyutMethod.sourceCode)
        self.assertEqual(expectedLineCount, actualLineCount, 'Method source code not accurate')

    def testChangeSourceCode(self):
        pyutMethod:        PyutMethod = self._generateAMethod()
        #
        # This is NOT the recommended way to update the source code
        #
        pyutMethod.sourceCode.insert(2, '# I am a comment')
        expectedLineCount: int = 6
        actualLineCount:   int = len(pyutMethod.sourceCode)
        self.assertEqual(expectedLineCount, actualLineCount, 'Method source code not accurate')

    def _generateAMethod(self) -> PyutMethod:
        pyutMethod: PyutMethod    = PyutMethod(name='OzzeeElGatoDiablo')

        pyutMethod.sourceCode = SourceCode(
            [
                'weLeft:           bool = True',
                'isOzzeeAGoodGato: bool = False',
                'if weLeft is True:',
                '    isOzzeeAGoodGato = True',
                'return isOzzeeAGoodGato'
            ]
        )
        return pyutMethod

    def _makeParameters(self) -> PyutParameters:

        pyutParameter1: PyutParameter  = PyutParameter(name='intParam', parameterType=PyutType("int"), defaultValue='0')
        pyutParameter2: PyutParameter  = PyutParameter(name='floatParam', parameterType=PyutType("float"), defaultValue='32.0')
        parameters:     PyutParameters = PyutParameters([pyutParameter1, pyutParameter2])

        return parameters

    def _makeSimpleParameters(self) -> PyutParameters:
        """
        No types, no default values
        """
        intParameter:   PyutParameter  = PyutParameter(name='intParameter')
        floatParameter: PyutParameter  = PyutParameter(name='floatParameter')
        boolParameter:  PyutParameter  = PyutParameter(name='boolParameter')

        parameters:     PyutParameters = PyutParameters([intParameter, floatParameter, boolParameter])

        return parameters

def suite() -> TestSuite:

    import unittest

    testSuite: TestSuite = TestSuite()

    testSuite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(testCaseClass=TestPyutMethod))

    return testSuite



if __name__ == '__main__':
    unitTestMain()

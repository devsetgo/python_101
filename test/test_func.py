from unittest import TestCase
from lesson_2.func import aFunction, aLoop, aFunc_1, aFunc_2, anIf

class TestAFunction(TestCase):

    def test_aFunction(self):
        testCase = {'expectedResult': 3}
        result = aFunction()
        assert result == testCase['expectedResult']

    def test_aFunction(self):
        testCase = {'expectedResult': 100}
        result = aLoop()
        assert result == testCase['expectedResult']

    def test_aFunc_1(self):
        testCase = {'mynum': 100,'expectedResult': 101}
        result = aFunc_1(testCase['mynum'])
        assert result == testCase['expectedResult']

    def test_aFunc_2(self):
        testCase = {'var': 100, 'expectedResult': 101}
        result = aFunc_2(testCase['var'])
        assert result == testCase['expectedResult']

    def test_anIf_1(self):
        testCase = {'alang': 'Python', 'expectedResult': 'cool'}
        result = anIf(testCase['alang'])
        assert result == testCase['expectedResult']

    def test_anIf_2(self):
        testCase = {'alang': 'JAVA', 'expectedResult': 'not as cool as Python'}
        result = anIf(testCase['alang'])
        assert result == testCase['expectedResult']

    def test_anIf_3(self):
        testCase = {'alang': 'C++', 'expectedResult': 'You should have picked Python'}
        result = anIf(testCase['alang'])
        assert result == testCase['expectedResult']

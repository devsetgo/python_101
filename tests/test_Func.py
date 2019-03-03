from unittest import TestCase
from lesson_2.func import aFunction, aLoop, aFunc_1, aFunc_2, anIf

class TestFunc(TestCase):
    def test_aFunction(self):

        testCase = {'expectedResult': 3}
        result = aFunction()
        assert result == testCase['expectedResult']

    def test_aLoop(self):

        testCase = {'expectedResult': 100}
        result = aLoop()
        assert result == testCase['expectedResult']

    def test_aFunc_1(self):

        testCase = {'mynum': 1, 'expectedResult': 2}
        result = aFunc_1(testCase['mynum'])
        assert result == testCase['expectedResult']

    def test_aFunc_1_fail(self):

        testCase = {'mynum': 1.2, 'expectedResult': 2.2}
        result = aFunc_1(testCase['mynum'])
        assert result == testCase['expectedResult']

    def test_aIf_1(self):

        testCase = {'lang': 'Python', 'expectedResult': 'cool'}
        result = anIf(testCase['lang'])
        assert result == testCase['expectedResult']

    def test_aIf_2(self):

        testCase = {'lang': 'JAVA', 'expectedResult': 'not as cool as Python'}
        result = anIf(testCase['lang'])
        assert result == testCase['expectedResult']

    def test_aIf_3(self):

        testCase = {'lang': 'C++', 'expectedResult': 'You should have picked Python'}
        result = anIf(testCase['lang'])
        assert result == testCase['expectedResult']
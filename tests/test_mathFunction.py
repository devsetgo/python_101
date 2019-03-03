from unittest import TestCase
from lesson_2.mathFunc import mathFunction

class TestMathFunction(TestCase):
    def test_add_mathFunction(self):
        # self.fail()
        testCase = {'v1': 2, 'v2': 2, 'type': 'add', 'expectedResult': 4}
        result = mathFunction(testCase['v1'], testCase['v2'], testCase['type'])
        assert result == testCase['expectedResult']

    def test_sub_mathFunction(self):
        # self.fail()
        testCase = {'v1': 4, 'v2': 2, 'type': 'sub', 'expectedResult': 2}
        result = mathFunction(testCase['v1'], testCase['v2'], testCase['type'])
        assert result == testCase['expectedResult']

    def test_mult_mathFunction(self):
        # self.fail()
        testCase = {'v1': 4, 'v2': 2, 'type': 'mult', 'expectedResult': 8}
        result = mathFunction(testCase['v1'], testCase['v2'], testCase['type'])
        assert result == testCase['expectedResult']

    def test_div_mathFunction(self):
        # self.fail()
        testCase = {'v1': 4, 'v2': 2, 'type': 'div', 'expectedResult': 2}
        result = mathFunction(testCase['v1'], testCase['v2'], testCase['type'])
        assert result == testCase['expectedResult']

    def test_div_error_mathFunction(self):
        # self.fail()
        testCase = {'v1': 4, 'v2': 0, 'type': 'div', 'expectedResult': 'Error: division by zero'}
        result = mathFunction(testCase['v1'], testCase['v2'], testCase['type'])
        assert result == testCase['expectedResult']

    def test_remainder_mathFunction(self):
        # self.fail()
        testCase = {'v1': 4, 'v2': 0, 'type': 'bob', 'expectedResult': 'not a currently support math type'}
        result = mathFunction(testCase['v1'], testCase['v2'], testCase['type'])
        assert result == testCase['expectedResult']


from unittest import TestCase
from lesson_3.read import open_sample

class TestOpen_sample(TestCase):

    # TODO: fix file open issue
    def test_open_sample(self):

        testCase = {'expectedResult': 17}
        file_open = open_sample()
        result = file_open
        assert result == testCase['expectedResult']

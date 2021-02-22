import unittest
from app import TestUnitTests

class TestCases(unittest.TestCase):
    def test_Unit_Tests(self):
        self.assertEqual(TestUnitTests().test, "test passed...")

#run actual ut
if __name__ == '__main__':
    unittest.main()
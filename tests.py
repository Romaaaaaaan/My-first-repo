import unittest
from first_lab_algo import is_monotone

class TestIsMonotone(unittest.TestCase):
    def test_increasing_sequence(self):
        arr = [1, 2, 3, 4, 5]
        result = is_monotone(arr)
        self.assertEqual(result, True)

    def test_decreasing_sequence(self):
        arr = [5, 4, 3, 2, 1]
        result = is_monotone(arr)
        self.assertEqual(result, True)

    def test_non_monotone_sequence(self):
        arr = [1, 2, 2, 3, 2, 4]
        result = is_monotone(arr)
        self.assertEqual(result, False)

    def test_non_strictly_increasing_sequence(self):
        arr = [1, 2, 3, 4, 4, 4, 5]
        result = is_monotone(arr)
        self.assertEqual(result, True)

    def test_strictly_increasing_sequence(self):
        arr = [5, 4, 3, 2, 1, 2, 3, 4, 5]
        result = is_monotone(arr)
        self.assertEqual(result, False)

    def test_sequence(self):
        arr = [2, 2, 2, 2, 2]
        result = is_monotone(arr)
        self.assertEqual(result, True)

    def test_increasing_sequence(self):
        arr = [2, 2, 2, 2, 3]
        result = is_monotone(arr)
        self.assertEqual(result, True)

    def test_descending_sequence(self):
        arr = [2, 2, 2, 2, 1]
        result = is_monotone(arr)
        self.assertEqual(result, True)            

if __name__ == "__main__":
    unittest.main()

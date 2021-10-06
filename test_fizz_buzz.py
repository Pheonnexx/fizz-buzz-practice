import unittest

from fizzbuzz import fizz_buzz_output


class TestFizzBuzzOutput(unittest.TestCase):
    def test_divisible_by_three(self):
        # when divisible by three then Fizz is returned.
        result = fizz_buzz_output(9)

        self.assertEqual(result, "Fizz")

    def test_not_divisible_by_three_or_five(self):
        # when divisible by three then Fizz is returned.
        result = fizz_buzz_output(8)

        self.assertEqual(result, "Not Fizz")
    
    def test_divisible_by_five(self):
        # when divisible by five then Buzz is returned.
        result = fizz_buzz_output(10)

        self.assertEqual(result, "Buzz")

if __name__ == '__main__':
    unittest.main()
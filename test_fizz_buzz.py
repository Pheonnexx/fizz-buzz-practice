import unittest

from fizzbuzz import fizz_buzz_output


class TestFizzBuzzOutput(unittest.TestCase):
    def test_divisible_by_three(self):
        # When divisible by three then Fizz is returned.
        result = fizz_buzz_output(9)

        self.assertEqual(result, "Fizz")

    def test_not_divisible_by_three_or_five(self):
        # When not divisible by three or five then Not Fizz is returned.
        result = fizz_buzz_output(8)

        self.assertEqual(result, "Not Fizz")
    
    def test_divisible_by_five(self):
        # When divisible by five then Buzz is returned.
        result = fizz_buzz_output(10)

        self.assertEqual(result, "Buzz")

    def test_divisible_by_fifteen(self):
        # When divisible by 15 FizzBuzz is returned.
        result = fizz_buzz_output(15)

        self.assertEqual(result, "FizzBuzz")


if __name__ == '__main__':
    unittest.main()
import io
import unittest
import unittest.mock

from fizzbuzz import fizz_buzz_output, fizz_buzz_print_list


class TestFizzBuzzOutput(unittest.TestCase):
    def test_divisible_by_three(self):
        # When divisible by three then Fizz is returned.
        result = fizz_buzz_output(9)

        self.assertEqual(result, "Fizz")

    def test_not_divisible_by_three_or_five(self):
        # When not divisible by three or five then Not Fizz is returned.
        result = fizz_buzz_output(8)

        self.assertEqual(result, "")
    
    def test_divisible_by_five(self):
        # When divisible by five then Buzz is returned.
        result = fizz_buzz_output(10)

        self.assertEqual(result, "Buzz")

    def test_divisible_by_fifteen(self):
        # When divisible by 15 FizzBuzz is returned.
        result = fizz_buzz_output(15)

        self.assertEqual(result, "FizzBuzz")


class TestFizzBuzzListPrint(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_list_output(self, mock_stdout):
        # When given a list of numbers it outputs for each number.
        number_list = [1, 3, 8, 10, 15]
        expected_output = "1 \n3 Fizz\n8 \n10 Buzz\n15 FizzBuzz\n"
        
        fizz_buzz_print_list(number_list)

        self.assertEqual(mock_stdout.getvalue(), expected_output) 

if __name__ == '__main__':
    unittest.main()
def fizz_buzz_output(number):
    # Outputs the calculated fizzbuzz for a number
    if number % 15 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"

    return ""

def fizz_buzz_print_list(number_list):
    # Given a list of numbers will print the fizzbuzz output in the terminal.
    for number in number_list:
       print(str(number) + " " + fizz_buzz_output(number))

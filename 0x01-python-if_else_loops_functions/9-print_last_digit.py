#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10  # Get the absolute value of the number and find the remainder when divided by 10 (to get the last digit)
    print(last_digit)  # Print the last digit
    return last_digit  # Return the last digit

# Example usage:
print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)

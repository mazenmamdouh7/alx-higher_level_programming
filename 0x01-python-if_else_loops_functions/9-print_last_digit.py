#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, int):
        last_digit = abs(number) % 10
        print(last_digit)
        return last_digit
    else:
        raise ValueError("Input is not an integer")
try:
    print_last_digit(98)
except ValueError as e:
    print(f"Correct output - case: 98\n{e}")

try:
    result = print_last_digit(98)
    print(f"Correct output - case: 98 with return\nResult: {result}")
except ValueError as e:
    print(f"Correct output - case: 98 with return\n{e}")

try:
    result = print_last_digit(-98)
    print(f"Correct output - case: -98 with return\nResult: {result}")
except ValueError as e:
    print(f"Correct output - case: -98 with return\n{e}")

try:
    print_last_digit(0)
except ValueError as e:
    print(f"Correct output - case: 0\n{e}")

try:
    print_last_digit("Holberton")
except ValueError as e:
    print(f"Correct output - case: 'Holberton' => exception\n{e}")

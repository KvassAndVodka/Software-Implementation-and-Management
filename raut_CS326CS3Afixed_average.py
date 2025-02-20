# Javier M. Raut
# CS3A

#buggy_average.py

"""
The bug mentioned in the previous comments dictate on how the program will handle an
empty list. The program will raise ZeroDivisionError if the list is empty considering
that the program will divide the total sum of the numbers by the length of the list.

I resolved both issues by adding a condition in the calculate_average function which
checks if the list has contents, if it does it will proceed to calculate the average
as usual, but if it is empty, it will return 0.
"""

""" 
a. What did you learn about debugging in this activity?
I learned that debugging is a very importtant part in programming. Considering that
the program will not always work as it is intended to. Looking out for potential bugs
and fixing them is a must have skill in developing and maintaining software.

b. What coding practices do you think would help prevent similar bugs in the future?
Some of the coding practices which would help prevent similar bugs in the future are:
- Properly commenting and documenting the code.
- Writing clean and readable code.
- Using tools like debuggers and linters to catch potential bugs.
- Extensive testing of the code specially edge cases.
- Conducting code reviews with peers to get feedback on the code.
- Avoid over reliance on LLMs for code generation to have more understanding of the code.
These are just few of the practices that I've to learn the hard way and I'm certain that
it can greatly help in preventing similar bugs in the future.
"""

import random

def calculate_average(numbers):
    """Calculates the average of a list of numbers.

    Args:
        numbers: A list of numbers.

    Returns:
        The average of the numbers, or 0 if the list is empty.
    """

    if numbers:   # Resolved ZeroDivisionError by checking if list has elements
        total = 0
        for number in numbers:
            total += number     # Correctly adds each number to the total
        return total / len(numbers)
    else:
        return 0  # Return 0 if list is empty

def generate_random_numbers(count, max_value):
    """Generates a list of random numbers.

    Args:
        count: The number of random numbers to generate.
        max_value: The maximum value for the random numbers.

    Returns:
        A list of random numbers.
    """
    random_numbers = []
    for _ in range(count):
        random_numbers.append(random.randint(0, max_value))
    return random_numbers


def main():
    """Main function to demonstrate the average calculation."""
    num_count = 10  # Number of random numbers to generate
    max_rand_value = 100  # Maximum value for random numbers

    # Resolved by adding empty list handling in calculate_average function
    random_nums = generate_random_numbers(num_count, max_rand_value)

    # Resolved ZeroDivisionError by checking if the list is empty
    average = calculate_average(random_nums)

    print("Random Numbers:", random_nums)
    print("Average:", average)


if __name__ == "__main__":
    main()

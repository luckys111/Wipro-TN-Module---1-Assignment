# functions.py
# functions.py

def sum_list(numbers):
    return sum(numbers)

def reverse_string(s):
    return s[::-1]

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

def print_even(numbers):
    return [n for n in numbers if n % 2 == 0]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

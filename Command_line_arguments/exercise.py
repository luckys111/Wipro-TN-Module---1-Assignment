# cla_exercises.py

import sys

# ------------------------ Task 1 ------------------------
def sum_two_numbers():
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print(f"Sum of {a} and {b} is: {a + b}")
    except (IndexError, ValueError):
        print("❌ Please provide two integers as command line arguments.")
        print("Usage: python cla_exercises.py sum <num1> <num2>")

# ------------------------ Task 2 ------------------------
def welcome_message():
    try:
        message = sys.argv[2]
        filename = sys.argv[3]
        print(f"Welcome Message: {message}")
        print(f"Filename: {filename}")
    except IndexError:
        print("❌ Please provide a welcome message and filename.")
        print("Usage: python cla_exercises.py welcome <message> <filename>")

# ------------------------ Task 3 ------------------------
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def sum_primes():
    try:
        numbers = list(map(int, sys.argv[2:]))
        if len(numbers) != 10:
            raise ValueError("You must provide exactly 10 numbers.")
        prime_sum = sum(num for num in numbers if is_prime(num))
        print(f"Sum of prime numbers: {prime_sum}")
    except ValueError as ve:
        print("❌", ve)
        print("Usage: python cla_exercises.py primes <10 space-separated integers>")

# ------------------------ Entry Point ------------------------
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please specify an operation: sum | welcome | primes")
        sys.exit(1)

    operation = sys.argv[1]

    if operation == "sum":
        sum_two_numbers()
    elif operation == "welcome":
        welcome_message()
    elif operation == "primes":
        sum_primes()
    else:
        print("❌ Invalid operation. Use: sum | welcome | primes")

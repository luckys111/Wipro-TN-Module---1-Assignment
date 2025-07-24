# mini_project.py
# mini_project.py

from functions import sum_list, reverse_string, factorial, count_case, print_even, is_prime
from string_utils import ispalindrome, count_the_vowels, frequency_of_letters

# ---- Mini Project 1: Sort colors ----
def sort_colors(color_string):
    colors = color_string.split('-')
    colors.sort()
    return '-'.join(colors)

print("Mini Project 1 Output:")
print(sort_colors("green-red-yellow-black-white"))
print(sort_colors("PINK-BLUE-TAN-PURPLE"))

# ---- Mini Project 2: Test string_utils module ----
print("\nMini Project 2 Output:")
name1 = "bob"
print("Palindrome:" if ispalindrome(name1) else "Not a palindrome.")
print("Vowels:", count_the_vowels(name1))
print("Frequency:", frequency_of_letters(name1))

name2 = "marcel bentok tanaka"
print("Palindrome:" if ispalindrome(name2) else "Not a palindrome.")
print("Vowels:", count_the_vowels(name2))
print("Frequency:", frequency_of_letters(name2))

# ---- Exercises from functions.py ----
print("\nExercises Output:")
print("Sum:", sum_list([8, 2, 3, 0, 7]))
print("Reverse:", reverse_string("1234abcd"))
print("Factorial:", factorial(5))
u, l = count_case("abcABC")
print(f"Upper: {u}, Lower: {l}")
print("Even Numbers:", print_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print("Prime (7):", is_prime(7))

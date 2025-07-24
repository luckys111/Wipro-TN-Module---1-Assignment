# Q1. Check if a given number is Positive, Negative or Zero
num = float(input("Q1 - Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q2. Check if a given number is Odd or Even
num = int(input("\nQ2 - Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3. Given two non-negative values, print true if they have the same last digit
a = int(input("\nQ3 - Enter first number: "))
b = int(input("Enter second number: "))
if a>=0 and b>0 and a % 10 == b % 10:
    print("True")
else:
    print("False")

# Q4. Print numbers from 1 to 10 in a single row with tab space
print("\nQ4 - Numbers from 1 to 10:")
for i in range(1, 11):
    print(i, end="\t")
print()

# Q5. Print even numbers between 23 and 57, one per line
print("\nQ5 - Even numbers from 23 to 57:")
for i in range(23, 58):
    if i % 2 == 0:
        print(i)

# Q6. Check if a given number is prime or not
num = int(input("\nQ6 - Enter a number to check if it's prime: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

# Q7. Print prime numbers between 10 and 99
print("\nQ7 - Prime numbers between 10 and 99:")
for num in range(10, 100):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print()

# Q8. Print the sum of all the digits of a given number
num = int(input("\nQ8 - Enter a number: "))
total = 0
temp = num
while temp > 0:
    total += temp % 10
    temp = temp // 10
print("Sum of digits:", total)

# Q9. Reverse a given number and print
num = int(input("\nQ9 - Enter a number to reverse: "))
rev = 0
temp = num
while temp > 0:
    rev = rev * 10 + temp % 10
    temp = temp // 10
print("Reversed number:", rev)

# Q10. Check if a given number is palindrome
num = int(input("\nQ10 - Enter a number to check if it's palindrome: "))
original = num
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
if original == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

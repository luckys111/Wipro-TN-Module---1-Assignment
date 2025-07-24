# exception_exercises.py

# 1. Division with exception handling
def division():
    try:
        a = int(input("Enter numerator: "))
        b = int(input("Enter denominator: "))
        print("Result:", a / b)
    except ZeroDivisionError:
        print("❌ Cannot divide by zero.")
    except ValueError:
        print("❌ Invalid number input.")

# 2. Prime number check with exception
def prime_check():
    try:
        n = int(input("Enter a number: "))
        if n <= 1:
            print("Not a prime number")
        else:
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    print("Not a prime number")
                    return
            print("It is a prime number")
    except ValueError:
        print("❌ Enter a valid integer.")

# 3. File title-case display
def display_file_title_case():
    try:
        fname = input("Enter file name: ")
        with open(fname, 'r') as f:
            print("File content in Title Case:")
            for line in f:
                print(line.title(), end='')
    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print("❌ Error:", e)

# 4. Index and value validation from a list
def list_index_check():
    lst = list(range(10))  # List of 10 integers (0 to 9)
    try:
        index = int(input("Enter index (0 to 9): "))
        value = lst[index]
        print("Value at index:", value)
        print("Positive" if value > 0 else "Negative" if value < 0 else "Zero")
    except IndexError:
        print("Index out of range.")
    except ValueError:
        print("Enter a valid integer.")


# Uncomment one-by-one to test
# division()
# prime_check()
# display_file_title_case()
# list_index_check()

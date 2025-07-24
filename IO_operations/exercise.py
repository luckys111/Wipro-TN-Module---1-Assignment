# exercise.py
# io_exercises.py

# 1. Read and display full content from a txt file
def read_entire_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print("\n[Full Content]\n", content)
    except FileNotFoundError:
        print("❌ File not found.")

# 2. Read first n lines from a file (n as user input)
def read_n_lines(filename, n):
    try:
        with open(filename, 'r') as f:
            print(f"\n[First {n} lines]")
            for i in range(n):
                line = f.readline()
                if line:
                    print(line.strip())
    except FileNotFoundError:
        print("❌ File not found.")

# 3. Accept input from user and append to file
def append_to_file(filename):
    try:
        line = input("Enter text to append to file: ")
        with open(filename, 'a') as f:
            f.write(line + "\n")
            print("✅ Line appended.")
    except Exception as e:
        print("❌ Error:", e)

# 4. Read file line by line and store into a list
def file_lines_to_list(filename):
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            print("\n[List of lines]:", lines)
            return lines
    except FileNotFoundError:
        print("❌ File not found.")
        return []

# 5. Find longest word (only one longest word guaranteed)
def find_longest_word(filename):
    try:
        with open(filename, 'r') as f:
            words = f.read().split()
            longest = max(words, key=len)
            print("\nLongest word:", longest)
    except FileNotFoundError:
        print("❌ File not found.")
    except ValueError:
        print("❌ File is empty or contains no words.")

# 6. Count frequency of user-entered word in file
def word_frequency(filename):
    try:
        target = input("Enter word to count frequency: ").lower()
        with open(filename, 'r') as f:
            words = f.read().lower().split()
            count = words.count(target)
            print(f"Frequency of '{target}': {count}")
    except FileNotFoundError:
        print("❌ File not found.")


# -----------------------
# Driver Menu to Test All
# -----------------------
if __name__ == "__main__":
    fname = input("Enter filename: ")

    print("\n--- I/O File Handling Options ---")
    print("1. Read entire file")
    print("2. Read first N lines")
    print("3. Append input to file")
    print("4. Store file lines into list")
    print("5. Find longest word")
    print("6. Word frequency count")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        read_entire_file(fname)
    elif choice == 2:
        n = int(input("Enter number of lines to read: "))
        read_n_lines(fname, n)
    elif choice == 3:
        append_to_file(fname)
    elif choice == 4:
        file_lines_to_list(fname)
    elif choice == 5:
        find_longest_word(fname)
    elif choice == 6:
        word_frequency(fname)
    else:
        print("❌ Invalid option.")

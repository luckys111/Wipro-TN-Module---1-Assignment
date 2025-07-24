# mini_project.py
# io_mini_project.py

from collections import Counter

def find_secret(filename):
    try:
        with open(filename, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]
            num_lines = len(lines)

            # Calculate meeting time
            if num_lines > 12:
                meeting_hour = num_lines % 12
                meeting_hour = 12 if meeting_hour == 0 else meeting_hour
                time = f"{meeting_hour} PM"
            else:
                time = f"{num_lines} AM"

            # Count words (case-insensitive)
            words = []
            for line in lines:
                words.extend(line.lower().split())
            word_counts = Counter(words)
            most_common_word, _ = word_counts.most_common(1)[0]

            # Capitalize first letter for street name
            location = f"{most_common_word.capitalize()} Street"

            print("\n✅ Secret Message:")
            print("Meeting time:", time)
            print("Meeting place:", location)

    except FileNotFoundError:
        print("❌ File not found.")
    except Exception as e:
        print("❌ Error:", e)

# Run the function
if __name__ == "__main__":
    filename = input("Enter the file name (e.g. sample.txt): ")
    find_secret(filename)

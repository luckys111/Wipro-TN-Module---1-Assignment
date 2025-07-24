# mini project.py 

import sys

def calculate_happiness(liked_str, disliked_str, given_str):
    liked = set(liked_str.split('-'))
    disliked = set(disliked_str.split('-'))
    given = given_str.split('-')

    happiness = 0

    for number in given:
        if number in liked:
            happiness += 1
        elif number in disliked:
            happiness -= 1
        # If the number is in neither, do nothing

    return happiness


def main():
    if len(sys.argv) != 4:
        print("Usage: python happiness.py <liked_numbers> <disliked_numbers> <given_numbers>")
        print("Example: python happiness.py 3-1 5-7 1-5-3-8")
        sys.exit(1)

    liked_numbers = sys.argv[1]
    disliked_numbers = sys.argv[2]
    given_numbers = sys.argv[3]

    final_happiness = calculate_happiness(liked_numbers, disliked_numbers, given_numbers)
    print("Final happiness is:", final_happiness)


if __name__ == "__main__":
    main()

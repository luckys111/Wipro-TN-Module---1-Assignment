#Mini Project 1: People and facts
people_facts = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

# Display original facts
print("Initial People and Facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

# Modify one fact and add a new one
people_facts["Jeff"] = "Is afraid of heights."
people_facts["Jill"] = "Can hula dance."

# Display updated dictionary
print("\nUpdated People and Facts:")
for person, fact in people_facts.items():
    print(f"{person}: {fact}")
    
    
    

# Mini Project 2: Find the Runner-Up Score
scores = [2, 3, 6, 6, 5]
unique_scores = list(set(scores))  # Remove duplicates
unique_scores.sort(reverse=True)   # Sort descending

if len(unique_scores) >= 2:
    print("Runner-Up Score:", unique_scores[1])
else:
    print("Not enough unique scores to determine runner-up.")



# Mini Project 3: Find the Percentage
records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a student name: ")
if name in records:
    marks = records[name]
    average = sum(marks) / len(marks)
    print(f"Average percentage mark for {name}: {average}")
else:
    print(f"Student '{name}' not found.")



# Mini Project 4: Find the Name
input_string = "Hi Alex WelcomeAlex Bye Alex."
target_name = "Alex"
count = input_string.count(target_name)

print(f"{target_name} appears {count} times.")

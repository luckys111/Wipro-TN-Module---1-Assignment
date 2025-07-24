# MINI PROJECT 1 - Travel Suggestion Based on Distance
distance = float(input("\nMini Project 1 - How far would you like to travel in miles? "))
if distance < 3:
    print("I suggest Bicycle to your destination")
elif distance < 300:
    print("I suggest Motor-cycle to your destination")
else:
    print("I suggest Super-Car to your destination")

# MINI PROJECT 2 - Server Cost Calculator
rate_per_hour = 0.51
hours_per_day = 24
daily_cost = rate_per_hour * hours_per_day
weekly_cost = daily_cost * 7
monthly_cost = daily_cost * 30
budget = 918
days_with_budget = budget / daily_cost

print("\nMini Project 2 - Server Cost Estimation")
print(f"Cost per day: ${daily_cost:.2f}")
print(f"Cost per week: ${weekly_cost:.2f}")
print(f"Cost per month: ${monthly_cost:.2f}")
print(f"With $918, you can operate a server for approximately {int(days_with_budget)} days.")

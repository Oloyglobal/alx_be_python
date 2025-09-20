# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Base reminder using match-case
match priority:
    case "high":
        reminder = f"Reminder: Your task '{task}' is HIGH priority."
    case "medium":
        reminder = f"Reminder: Your task '{task}' is MEDIUM priority."
    case "low":
        reminder = f"Reminder: Your task '{task}' is LOW priority."
    case _:
        reminder = f"Reminder: Your task '{task}' has an UNKNOWN priority."

# Add note if time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Final output
print(reminder)

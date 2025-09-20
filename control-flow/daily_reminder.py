# daily_reminder.py

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority
match priority:
    case "high":
        message = f"Your task '{task}' is high priority."
    case "medium":
        message = f"Your task '{task}' is medium priority."
    case "low":
        message = f"Your task '{task}' is low priority."
    case _:
        message = f"Your task '{task}' has an unknown priority."

# Add time sensitivity
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# 🚨 MUST print directly starting with Reminder:
print(f"Reminder: {message}")

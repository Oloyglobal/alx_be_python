# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority-based response
match priority:
    case "high":
        reminder = f"⚡ High Priority: Don't forget to {task}."
    case "medium":
        reminder = f"📌 Medium Priority: Make sure you {task} today."
    case "low":
        reminder = f"📝 Low Priority: You should {task} when you have free time."
    case _:
        reminder = f"❓ Priority not recognized. Still, remember to {task}."

# Conditional check for time sensitivity
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Demonstrating loop: repeat reminder 3 times for emphasis
count = 0
while count < 3:
    print(reminder)
    count += 1

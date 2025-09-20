task = input("Enter your task for today: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is this task time-bound? (yes or no): ").lower()
match priority:
    case "high":
        reminder = f"⚡ High Priority: Don't forget to {task}."
    case "medium":
        reminder = f"📌 Medium Priority: Make sure you {task} today."
    case "low":
        reminder = f"📝 Low Priority: You should {task} when you have free time."
    case _:
        reminder = f"❓ Priority not recognized. Still, remember to {task}."
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
count = 0
while count < 3:
    print(reminder)
    count += 1

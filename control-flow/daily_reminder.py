# Description: This script prompts the user to input a task description, priority, and whether the task is time-bound.
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high-priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high-priority task. Schedule it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium-priority task that should be completed soon.")
        else:
            print(f"{task} is a medium-priority task. Complete it when feasible.")
    case "low":
        if time_bound == "yes":
            print(f"{task} is a low-priority task but has a deadline, so don't delay too long!")
        else:
            print(f"{task} is a low-priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please use 'high', 'medium', or 'low'.")
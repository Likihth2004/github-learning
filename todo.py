tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter a task: ").strip()
        if task:
            tasks.append({"name": task, "completed": False})
            print("Task added.")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for number, task in enumerate(tasks, start=1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{number}. {task['name']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks to complete.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task['name']}")

            try:
                task_number = int(input("Enter the task number to complete: "))
                if 1 <= task_number <= len(tasks):
                    tasks[task_number - 1]["completed"] = True
                    print("Task completed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")

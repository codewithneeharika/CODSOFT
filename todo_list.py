# To-Do List Application

tasks = []

print("📋 To-Do List Application")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("✅ Task added")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])

    elif choice == "3":
        task_no = int(input("Enter task number to delete: "))
        if 0 < task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print("❌ Removed:", removed)
        else:
            print("Invalid task number")

    elif choice == "4":
        print("👋 Exiting...")
        break

    else:
        print("Invalid choice")

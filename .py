tasks = []

def addtasks():
    task = input("Enter the new task: ")
    tasks.append(task)
    print("Task added successfully")

def viewtasks():
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f'{i + 1}. {task}')

def deletetask():
    if len(tasks) == 0:
        print("There are no tasks to delete")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f'{i + 1}. {task}')
        choice = int(input("Enter the task number to delete: "))
        if 0 < choice <= len(tasks):
            del tasks[choice - 1]
            print("Task deleted")
        else:
            print("Invalid task number")

def main():
    while True:
        print("\nTO-DO-LIST-APPLICATION")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Quit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            addtasks()
        elif choice == 2:
            viewtasks()
        elif choice == 3:
            deletetask()
        elif choice == 4:
            print("Thank you for using")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()

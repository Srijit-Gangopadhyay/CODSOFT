tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added successfully")


def view_tasks():
    if tasks:
        print("To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No task in the list.")


def remove_task():
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to remove: "))
            if 1 <= index <= len(tasks):
                removed_task = tasks.pop(index - 1)
                print(f"Task '{removed_task}' removed successfully")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
    else:
        print("No task in the list.")


while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")






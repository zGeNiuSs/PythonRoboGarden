import os

def display_menu():
    print("\nTask List Manager")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. View all tasks")
    print("4. Exit")

def add_task(file_path):
    try:
        with open(file_path, 'a') as file:
            task = input("Enter the new task: ")
            file.write(f"{task}\n")
            print("Task added successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def remove_task(file_path):
    try:
        if not os.path.exists(file_path):
            print("No tasks found.")
            return

        with open(file_path, 'r') as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found.")
            return

        print("\nCurrent Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task.strip()}")

        try:
            task_number = int(input("Enter the number of the task to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                with open(file_path, 'w') as file:
                    file.writelines(tasks)
                print(f"Task '{removed_task.strip()}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input: Please enter a numeric value.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied: Unable to read/write the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_tasks(file_path):
    try:
        if not os.path.exists(file_path):
            print("No tasks found.")
            return

        with open(file_path, 'r') as file:
            tasks = file.readlines()

        if tasks:
            print("\nCurrent Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task.strip()}")
        else:
            print("No tasks found.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = "Python Tutorial/Task List Manager/tasks.txt"

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(file_path)
        elif choice == '2':
            remove_task(file_path)
        elif choice == '3':
            view_tasks(file_path)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
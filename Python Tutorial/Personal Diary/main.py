import os
from datetime import datetime

def display_menu():
    print("\nPersonal Diary Application")
    print("1. Write a new entry")
    print("2. View previous entries")
    print("3. Exit")

def write_entry(file_name):
    try:
        with open(file_name, 'a') as file:
            entry = input("Write your entry: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{timestamp} - {entry}\n")
            print("Entry saved successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_entries(file_name):
    try:
        if not os.path.exists(file_name):
            print("No entries found.")
            return

        with open(file_name, 'r') as file:
            entries = file.readlines()
            if entries:
                print("\nPrevious Entries:")
                for entry in entries:
                    print(entry.strip())
            else:
                print("No entries found.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = "Python Tutorial/Personal Diary/diary.txt"

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            write_entry(file_name)
        elif choice == '2':
            view_entries(file_name)
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()

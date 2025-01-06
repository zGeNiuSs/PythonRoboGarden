import os

def display_menu():
    print("\nStudent Grade Tracker")
    print("1. Input and store subject grades")
    print("2. Calculate and display average grade")
    print("3. Exit")

def input_and_store_grades(file_name):
    try:
        with open(file_name, 'a') as file:
            while True:
                subject = input("Enter the subject (or type 'done' to finish): ")
                if subject.lower() == 'done':
                    break
                try:
                    grade = float(input(f"Enter the grade for {subject}: "))
                    file.write(f"{subject},{grade}\n")
                    print(f"Grade for {subject} saved successfully.")
                except ValueError:
                    print("Invalid input: Please enter a numeric grade.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_and_display_average(file_name):
    try:
        if not os.path.exists(file_name):
            print("No grades found.")
            return

        with open(file_name, 'r') as file:
            grades = []
            for line in file:
                try:
                    subject, grade = line.strip().split(',')
                    grades.append(float(grade))
                except ValueError:
                    print(f"Invalid data format in file: {line.strip()}")

            if grades:
                average_grade = sum(grades) / len(grades)
                print(f"\nAverage Grade: {average_grade:.2f}")
            else:
                print("No valid grades found.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = "Python Tutorial/Student Grade Tracker/grades.txt"

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            input_and_store_grades(file_name)
        elif choice == '2':
            calculate_and_display_average(file_name)
        elif choice == '3':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


main()
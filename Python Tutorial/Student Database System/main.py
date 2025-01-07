class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def calculate_average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

students = []

def add_student():
    name = input("Enter the student's name: ")
    age = int(input("Enter the student's age: "))
    grades = list(map(float, input("Enter the student's grades (separated by spaces): ").split()))
    student = Student(name, age, grades)
    students.append(student)
    print("Student added successfully!\n")

def display_all_students():
    if not students:
        print("No students in the database.\n")
    else:
        for i, student in enumerate(students, 1):
            print(f"Student {i}:")
            student.display_info()
            print(f"Average Grade: {student.calculate_average_grade():.2f}\n")

def main():
    while True:
        print("Student Database System")
        print("1. Add a Student")
        print("2. Display All Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()

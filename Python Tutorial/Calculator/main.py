
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

sum = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number

# Handle division to avoid division by zero
if second_number != 0:
    division = first_number / second_number
else:
    division = "cannot divide by zero"

print(f"Sum: {sum}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")

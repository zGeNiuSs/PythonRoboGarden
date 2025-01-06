def fibonacci(n):
    # Base cases: fibonacci(0) is 0, fibonacci(1) is 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
number = 5
print(f"The {number}th Fibonacci number is {fibonacci(number)}")
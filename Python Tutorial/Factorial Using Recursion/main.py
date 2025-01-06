def factorial(n):

    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

number = 5
print(f"The factorial of {number} is {factorial(number)}")
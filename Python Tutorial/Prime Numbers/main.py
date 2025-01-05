n = int(input("Enter a number N to find prime numbers between 2 and N: "))

print(f"Prime numbers between 2 and {n}:")
for num in range(2, n + 1):

    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

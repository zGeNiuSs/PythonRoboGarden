seq = int(input("Enter the number of terms in the Fibonacci sequence: "))

a = 0
b = 1

print("Fibonacci sequence:")
for i in range(seq):
    print(a)
    temp = a
    a = b
    b = temp + b

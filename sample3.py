# Function for nth Fibonacci number

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Driver Program

n = 10
result = fibonacci(n)

print(f"Fibonacci number at position {n} is {result}")

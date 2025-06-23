# Get input from user
num = int(input("Enter a number: "))
factorial = 1

# Check if number is negative
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is: {factorial}")

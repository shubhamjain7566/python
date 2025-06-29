import math

try:
    num = float(input("Enter a number: "))

    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
    sin_result = math.sin(num)  # Input is in radians

    print(f"\nResults for {num}:")
    print(f"Square root: {sqrt_result}")
    print(f"Natural logarithm (log base e): {log_result}")
    print(f"Sine (in radians): {sin_result}")

except ValueError:
    print("Please enter a valid number greater than 0 for logarithm and square root.")
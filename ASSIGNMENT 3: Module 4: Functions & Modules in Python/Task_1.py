try :
    def factorial(n):
        if n < 2:
            return 1
        return n * factorial(n - 1)

    number = int(input("Enter a number: "))
    print(f"Factorial of {number} is: ", factorial(number))
except ValueError:
    print("Invalid input. Please enter numeric values.")
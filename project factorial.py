def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

def main():
    num_str = input("Enter a non-negative integer: ")

    try:
        num = int(num_str)
        if num < 0:
            raise ValueError("Please enter a non-negative integer.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    result = factorial(num)

    print(f"The factorial of {num} is: {result}")

    parity = check_even_odd(result)
    print(f"The factorial result is {parity}.")

if __name__ == "__main__":
    main()

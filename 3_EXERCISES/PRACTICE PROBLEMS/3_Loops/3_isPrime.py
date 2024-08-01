# Program to check whether a number is prime or composite
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
number = int(input("Enter a number to check if it is prime or composite: "))
if number <= 1:
    print(f"{number} is neither prime nor composite.")
elif is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is a composite number.")

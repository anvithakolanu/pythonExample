def is_prime(n):
    # Handle edge cases
    if n <= 1:
        return False
    # Check for factors up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Predefined number to check
num = 29  # You can change this to any number you want to check

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(start):
    """Find and print prime numbers starting from a given number."""
    n = start
    while True:
        if is_prime(n):
            print(f"Prime found: {n}")
        n += 1

# Start finding primes from a high number
start_number = 10**12  # You can adjust this to any high number
find_primes(start_number)
import numpy as np

def euler_phi(n):
    result = n  # Initialize result to n
    # Check for each integer up to sqrt(n)
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            # If i is a factor, apply the Phi formula
            while n % i == 0:
                n //= i
            result *= (1 - 1 / i)
    # If n is a prime number greater than sqrt(n), apply the formula
    if n > 1:
        result *= (1 - 1 / n)
    return int(result)

# Test case
print(euler_phi(15))  # Output should be 8

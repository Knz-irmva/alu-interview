#!/usr/bin/python3

def minOperations(n):
    if n == 1:
        return 0
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    
    return n  # If n is prime, return n itself

# Example usage:
n = 9
result = minOperations(n)
print(f"Number of operations to get {n} H characters: {result}")


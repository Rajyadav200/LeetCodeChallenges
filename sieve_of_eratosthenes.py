#   This Python script implements the Sieve of Eratosthenes algorithm to find prime numbers within a given range.
#   Time complexity: O(end log(log(end)))
#   Space complexity: O(end)

def sieve_of_eratosthenes(start, end):
    # Create a list to mark prime numbers, initialized to 1 (True)
    prime_flags = [1] * (end + 1)
    
    # Iterate over numbers from 2 to the square root of the end value
    for i in range(2, int(end**0.5) + 1):
        if prime_flags[i]:  # Check if the number is marked as prime,

            # Mark multiples of the number as non-prime
            for j in range(i**2, end + 1, i):
                prime_flags[j] = 0
                
    # Create a list of prime numbers within the given range
    prime_numbers = [index for index, flag in enumerate(prime_flags) if flag and index > 1]
    return prime_numbers

# Example usage
primes = sieve_of_eratosthenes(0, 8)
print(primes)

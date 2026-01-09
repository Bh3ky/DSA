# a natural prime is called a prime if it is bigger than 1 and has no
# divisors other than 1 and itself. 

"""
PROBLEM: Write a program that takes an integer argument and return all the
primes between 1 and that integer. For example, if the input is 18, we should
return [2,3,5,7,11,13,17]

Hint: exclude the multiple primes
"""

# First approach: sifting approach
def generate_primes(n): 
    primes = []
    # is_prime[p] represents if p is prime or not. initially, set each to
    # true, expecting 0 and 1. then use sieving to eliminate nonprimes.
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n):
        if is_prime[p]:
            primes.append(p)
            # sieve p's multiples
            for i in range(p, n + 1, p):
                is_prime[i] = False

    return primes

# Note: justify the sifting approach over the trial-division algorithm on heuristic
# grounds. the time to sift out the multiples of p yields an O(nloglogn) time bound.
# the space complexity is dominated by the storage for P i.e., O(n)


# Second optimised approach: improved runtime by sieving p's multiples from p^2 instead
# p since all numbers of the kp where k < p have already been sieved out.
# storage can be reduced by ignoring even numbers.

def generate_primes_from_1_to_n(n):
    size = (n - 3) // 2 + 1
    primes = [2] # stores the primes from 1 to n
    # is_prime[i] represents (2i + 3) is prime or not.
    # initially set each to true. then use sieving to elimate nonprimes.
    is_prime = [True] * size
    for i in range(size):
        if is_prime[i]:
            p = i * 2 + 3
            primes.append(p)
            # sieving from p^2, where p^2 = (4i^2 + 12i + 9). the index in
            # is_prime is (2i^2 + 6i + 3) because is_prim3[i] is represents
            # 2i + 3.
            # Note that we need to use long for j because p^2 might overflow.
            for j in range(2 * i**2 + 6 * i + 3, size, p):
                is_prime[j] = False

    return primes
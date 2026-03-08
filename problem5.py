#problem5.py
#Name:Gavin Grow
#Date:3/1/26
#Assignment:Problem 5

from NumberTests import isPrime

def getPrimeFactors(n):
    """Returns a list of prime factors of n with multiplicity."""
    factors = []
    # Handle factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Handle odd factors
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def lcmUpTo(n):
    """Returns the LCM of all numbers from 1 to n."""
    from collections import defaultdict
    max_exp = defaultdict(int)
    for i in range(2, n + 1):
        factors = getPrimeFactors(i)
        exp_count = {}
        for f in factors:
            exp_count[f] = exp_count.get(f, 0) + 1
        for prime, exp in exp_count.items():
            if exp > max_exp[prime]:
                max_exp[prime] = exp
    result = 1
    for prime, exp in max_exp.items():
        result *= prime ** exp
    return result

def main():
    result = lcmUpTo(20)
    print(f"The smallest positive number that is evenly divisible by all numbers from 1 to 20 is {result}.")

if __name__ == "__main__":
    main()

#problem4.py
#Name:Gavin Grow
#Date:3/8/26
#Assignment:problem4
def isPalindrome(n):
    """Returns True if the number is a palindrome, False otherwise."""
    s = str(n)
    return s == s[::-1]

def findLargestPalindrome():
    """Finds the largest palindrome made from the product of two 3-digit numbers."""
    max_palindrome = 0
    factors = (0, 0)
    
    # Start from highest 3-digit numbers to find largest first
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            product = i * j
            if isPalindrome(product) and product > max_palindrome:
                max_palindrome = product
                factors = (i, j)
    
    return max_palindrome, factors

# Main function to run the program
def main():
    result, factors = findLargestPalindrome()
    print(f"The largest palindrome is {result}, which is the product of {factors[0]} and {factors[1]}.")

if __name__ == "__main__":
    main()

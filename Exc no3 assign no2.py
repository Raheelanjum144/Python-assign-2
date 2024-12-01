#Write a function to find the factorial of a number using recursion.

#In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n.

# For example, 5! = 5 × 4 × 3 × 2 × 1 = 120.  

def factorial(n):


  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers.")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)

# Example usage:
number = 10
result = factorial(number)
print(f"The factorial of {number} is {result}") 


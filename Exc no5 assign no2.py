# reate a function to check if a given number is prime.
# A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# In simpler terms, a prime number is only divisible by 1 and itself

def is_prime(num):
  """Checks if a number is prime.

  Args:
    num: The number to check.

  Returns:
    True if the number is prime, False otherwise.
  """

  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

# Example usage:
number = 23
if is_prime(number):
  print(f"{number} is a prime number.")
else:
  print(f"{number} is not a prime number.")
# Write a function to count the vowels in a given string.
# Vowels are the letters in the alphabet that represent speech sounds where air leaves the mouth without any blockage by the tongue, lips, or throat.
#The vowels in the alphabet are a, e, i, o, u, and someti

def count_vowels(string):
  """Counts the number of vowels in a given string.

  Args:
    string: The input string.

  Returns:
    The number of vowels in the string.
  """

  vowels = "aeiouAEIOU"
  count = 0
  for char in string:
    if char in vowels:
      count += 1
  return count

# Example usage:
string = "How are you!"
vowel_count = count_vowels(string)
print("Number of vowels:", vowel_count)
#Write a function that takes a string and returns it reversed.
# The provided Python function reverse_string(string) takes a string as input and returns its reversed version. 
def reverse_string(string):

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

# Example usage:
input_string = " Raheel Anjum"
result = reverse_string(input_string)
print(result)
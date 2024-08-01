# WAP to remove vowels from a string


input_string = input("Enter a string to remove vowels from: ")
vowels = "aeiouAEIOU"

# Initialize an empty string for the result
result_string = ""

# Iterate over each character in the input string
for char in input_string:
    # Append character to result_string if it is not a vowel
    if char not in vowels:
        result_string += char


print("String after removing vowels:", result_string)

# write a Program to reverse a string using a for loop


input_string = input("Enter a string to reverse: ")

# Initialize an empty string for the reversed result
reversed_string = ""

# Iterate over the string in reverse order using a for loop
for char in input_string:
    reversed_string = char + reversed_string

print("Reversed string:", reversed_string)

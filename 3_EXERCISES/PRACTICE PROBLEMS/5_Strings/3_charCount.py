# write a Program to find the count of a given character in a string


input_string = input("Enter a string: ")
char_to_count = input("Enter the character to count: ")

count = 0

# Iterate over each character in the input string
for char in input_string:
    # Increment count if character matches char_to_count
    if char == char_to_count:
        count += 1

print(f"The count of character '{char_to_count}' is:", count)

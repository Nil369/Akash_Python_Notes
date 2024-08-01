# WRITE A PROGRAM in Python to print Palindrome or not.


string = input("Enter a word: ")


# Remove spaces and convert to lowercase for uniformity
cleaned_string = string.replace(" ", "").lower()

reversed_string = cleaned_string[::-1]


# Check palindrome by comparing the strings
is_palindrome = cleaned_string == reversed_string


result = "is a palindrome" * is_palindrome + "is not a palindrome" * (not is_palindrome)
print(f"'{string}' {result}.")

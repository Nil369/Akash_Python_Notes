# STRINGS ARE IMMUTABLE => wE cannot change them by running functions on them 
# It will create a new string and run functions on them but the original string will be unharmed

name = "akash"
length = len(name)
print(length)  # Output: 5

lower_case = name.lower()
print(lower_case)  # Output: akash

upper_case = name.upper()
print(upper_case)  # Output: AKASH

capitalized = name.capitalize()
print(capitalized)  # Output: Akash

name_with_spaces = "  Akash  "
stripped = name_with_spaces.strip()
print(stripped)  # Output: Akash

position = name.find("k")
print(position)  # Output: 2

replaced = name.replace("k", "c")
print(replaced)  # Output: Acash

split_name = name.split("a")
print(split_name)  # Output: ['Ak', 'sh']

separator = "-"
joined_name = separator.join(name)
print(joined_name)  # Output: A-k-a-s-h

starts_with = name.startswith("A")
print(starts_with)  # Output: True

ends_with = name.endswith("h")
print(ends_with)  # Output: True


is_alnum = name.isalnum() # Returns True if all characters in the string are alphanumeric.
print(is_alnum)  # Output: True



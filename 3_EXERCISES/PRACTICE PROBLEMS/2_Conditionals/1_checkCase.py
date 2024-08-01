# WRITE A PROGRAM in Python that will check for the case of a character from the user and write a program accordingly.

n = input("Enter a word: ")

if(n.isupper()):
    print(f"{n} is in upper case.")
elif(n.islower()):
    print(f"{n} is in lower case.")
else:
    print(f"{n} is in mixed case or contains non-alphabetic characters.")
   
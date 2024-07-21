# String is a data type in python. 
# String is a sequence of characters enclosed in quotes. 
# We can primarily write a string in these three ways.

a ='Shruti'       # Single quoted string 
name = "Akash"      # Double quoted string 

# Triple quoted string 
c = '''Hi! I'm  
       Akash Halder'''  


# SLICING STRING IN PYTHON
nameshort = name[0:3] # start from index 0 all the way till 3 (excluding 3)
print(nameshort)

char1 = name[1]
print(char1)


# NEGETIVE STRING IN PYTHON
print(name[-4: -1])
print(name[1:4]) # Convert into corresponding positive indexes to evaluate

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])
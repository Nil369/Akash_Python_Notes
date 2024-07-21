# Dictionary is a collection of keys-value pairs in Python.

"""
PROPERTIES OF PYTHON DICTIONARIES:

1. It is unordered. 
2. It is mutable. 
3. It is indexed. 
4. Cannot contain duplicate keys. 

"""

d = {} # Empty dictionary

marks = {
    "Akash": 100,
    "Shruti": 97,
    "Shubham": 56,
    "Rohan": 23,
    "marks":[92,98,96]
}


print(marks, type(marks))
print(marks["Akash"])
# Can you change the values inside a list which is contained in set S? 
s = {8, 7, 12, "Akash", [1,2]}

"""
No, we cannot have a list as an element of a set in Python. This is because lists are mutable
and therefore not hashable, which is a requirement for all elements in a set. 
Sets rely on the immutability and hashability of their elements to efficiently manage and retrieve them.

If we try to create a set with a list as an element, Python will raise a TypeError like this:

TypeError: unhashable type: 'list'

"""
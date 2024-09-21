# 1. ITERABLES:
""" 
An iterable is any Python object that can return its elements one at a time. 
-> Examples include lists, tuples, strings, and dictionaries.
-> An object is considered iterable if it has an `__iter__()` method.
"""

my_list = [1, 2, 3, 4]
# The list `my_list` is iterable, meaning you can loop through its elements using a for loop.
for item in my_list:
    print(f"Iterable element: {item}")  

# 2. ITERATORS:
"""
An iterator is an object that represents a stream of data. 
-> It returns data, one element at a time, when called with `next()`.
-> An iterator object has both `__iter__()` and `__next__()` methods.
"""

# Convert the iterable `my_list` into an iterator using the `iter()` function.
my_iterator = iter(my_list)

# You can now manually access elements using `next()`.
print(f"First element: {next(my_iterator)}")  
print(f"Second element: {next(my_iterator)}")  
# If you keep calling `next()` after the last element, it raises a `StopIteration` exception.


# 3. ITERATIONS:
"""
Iteration is the process of accessing each element in an iterable object one by one.
# This is typically done using a for loop, but you can also manually iterate using `next()` with an iterator.
"""

# Using a for loop for iteration (automatic handling of `StopIteration`).
for element in my_list:
    print(f"Iteration element: {element}")  

# 4. GENERATORS:
"""
Generators are a special type of iterable, similar to functions, but they yield values one at a time using the `yield` keyword.
They are more memory efficient than lists because they generate items on the fly.
"""

def my_generator():
    yield 1
    yield 2
    yield 3

# The generator function returns a generator object.
gen = my_generator()
print(gen)
print(f"Generator first element: {next(gen)}") 

# Iterating over the rest of the generator using a for loop.
for value in gen:
    print(f"Remaining generator element: {value}")  

# Once all elements are consumed, the generator raises a `StopIteration` exception.
# Generators are especially useful for generating large sequences of values lazily.
# They are created using functions with the `yield` keyword or generator expressions.

# Example of a generator expression:
squares = (x * x for x in range(5))  
for square in squares:
    print(f"Square: {square}")  
    

# Summary:
"""
- Iterable: An object you can iterate over (e.g., lists, strings).
# - Iterator: An object representing a stream of data, returned by the `iter()` function.
# - Iteration: The process of looping over an iterable or using `next()` on an iterator.
# - Generator: A special function or expression that yields values lazily using `yield`.
"""


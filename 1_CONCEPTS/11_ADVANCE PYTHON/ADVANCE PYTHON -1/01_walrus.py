"""
Walrus Operator allows you to assign a value to a variable within an expression. 
This can be useful when you need to use a value multiple times in a loop,
but don’t want to repeat the calculation.
"""

# Using walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 
    
# Output: List is too long (5 elements, expected <= 3)
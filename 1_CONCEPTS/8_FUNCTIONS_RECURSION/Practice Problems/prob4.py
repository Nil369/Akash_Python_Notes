"""
Write a python function to print first n lines of the following pattern: 

*** 
**               
* 

"""

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    pattern(n-1)




input = int(input("Enter a number: "))
pattern(input)
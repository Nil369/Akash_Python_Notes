# Write a recursive function to calculate the sum of first n natural numbers.

def calculate_sum(n):
    if n == 0:
        return 0
    else:
        return n + calculate_sum(n-1)
    
a = int(input("Enter a number till you want sum of: "))
res = calculate_sum(a)
print(res)

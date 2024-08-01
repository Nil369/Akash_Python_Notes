"""
Program to print the given pattern
1
2 2 2
3 3 3 3 3
"""

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(2 * i - 1):
        print(i, end=' ')
    print()

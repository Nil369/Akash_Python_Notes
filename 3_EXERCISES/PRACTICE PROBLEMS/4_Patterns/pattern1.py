"""
Write a program in Python to print the following pattern
1
2 1 2
3 2 1 2 3

"""

rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    for j in range(2, i + 1):
        print(j, end=' ')
    print()

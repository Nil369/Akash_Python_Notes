"""
write a Program to print the given pattern:
AAAA
BBB
CC
D
"""

rows = int(input("Enter the number of rows: "))

for i in range(rows):
    for j in range(rows - i):
        print(chr(65 + i), end='')
    print()

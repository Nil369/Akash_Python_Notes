# Sum of first n numbers

from time import time


# sol1
# Functions
def func1(n):
    summ = 0
    for i in range(1, n + 1):
        summ += i
    return summ


# sol2
def func2(n):
    return int((n * (n + 1)) / 2)


# Program
x = int(input("Enter a number: "))
startTime = time()
# y1 = func1(x)
y2 = func2(x)
endTime = time()
totalTime = endTime - startTime
# print(y1)
# print(f"Total time taken for func1 to execute -> {totalTime}")

print(y2)
print(f"Total time taken for func2 to execute -> {totalTime}")

''' So we can clearly see that func 2 takes les time to execute so It's a better algorithm than func 1'''

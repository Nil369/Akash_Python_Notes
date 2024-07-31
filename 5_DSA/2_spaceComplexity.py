# Sum of first n numbers

import tracemalloc as tm


# sol1
def func1(n):
    summ = 0
    for i in range(1, n + 1):
        summ += i
    return summ


# sol2
def func2(n):
    return int((n * (n + 1)) / 2)


if __name__ == '__main__':
    x = int(input("Enter a number: "))
    tm.start()
    # y1 = func1(x)
    y2 = func2(x)

    # print(y1)
    # print(tm.get_traced_memory())

    print(y2)
    print(tm.get_traced_memory())


    tm.stop()

    ''' So we can clearly see that func 2 takes les space. So It's a better algorithm than func 1'''

# Time - Space tradeOff  => Time of execution is inversely proportional to space/ memory usage in the algorithm.
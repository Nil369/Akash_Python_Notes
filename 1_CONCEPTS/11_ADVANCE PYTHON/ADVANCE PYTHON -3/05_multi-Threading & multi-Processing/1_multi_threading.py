"""
Multithreading is a technique where multiple threads are spawned by a process to execute tasks concurrently. 
Threads share the same memory space and resources of the parent process, making it easy to share data between them. 
However, in Python, multithreading has some limitations due to the Global Interpreter Lock (GIL).

💡Key Concepts:

-> Thread: The smallest unit of a process that can be scheduled and executed independently.

-> Global Interpreter Lock (GIL): A mutex that allows only one thread to execute Python bytecode at a time, 
                                  which means that even in a multithreaded program, only one thread can execute 
                                  Python code simultaneously. This can be a limitation for CPU-bound tasks.


🪴 Use Cases: Best suited for I/O-bound tasks like file I/O, network requests, or database operations, 
where threads can be idle while waiting for I/O operations to complete.

"""


import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(1)
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(1)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))
t2= threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
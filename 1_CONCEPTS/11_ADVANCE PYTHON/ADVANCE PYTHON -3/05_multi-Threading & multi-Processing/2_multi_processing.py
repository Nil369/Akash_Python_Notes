"""
Multiprocessing is a technique where multiple processes are created to execute tasks concurrently.
Each process has its own memory space, which avoids issues like GIL, making it suitable for CPU-bound tasks.

💡Key Concepts:
-> Process: An independent execution unit that has its own memory space.

-> No GIL Limitation: Each process runs in its own Python interpreter, 
so the GIL does not limit the parallel execution of Python code.

-> Inter-Process Communication (IPC): Processes don't share memory space, 
so you need mechanisms like pipes, queues, or shared memory to share data.

🪴 Use Cases: Best suited for CPU-bound tasks like mathematical computations, image processing, or data analysis.

"""

import multiprocessing
import time

# Function to simulate a time-consuming task
def process_task(name, duration):
    print(f"{name} started, will take {duration} seconds.")
    time.sleep(duration)
    print(f"{name} finished.")

if __name__ == "__main__":
    # Define processes with different sleep durations
    process1 = multiprocessing.Process(target=process_task, args=("Process 1", 2))
    process2 = multiprocessing.Process(target=process_task, args=("Process 2", 3))
    process3 = multiprocessing.Process(target=process_task, args=("Process 3", 1))
    
    start_time = time.time()
    
    # Start processes
    process1.start()
    process2.start()
    process3.start()
    
    # Wait for all processes to complete
    process1.join()
    process2.join()
    process3.join()
    
    end_time = time.time()
    print(f"All processes finished. Total time taken: {end_time - start_time:.2f} seconds")

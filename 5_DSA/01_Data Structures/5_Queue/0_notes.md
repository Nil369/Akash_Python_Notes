# Queue Data Structure


A **`Queue`** is a linear data structure that operates on a **`First In First Out (FIFO)`** principle. This means that the first element added to the queue will be the first one to be removed.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20221209094646/Queue-768.png">

### Definition:
A queue can be visualized as a list where:
- **Insertions** are made at the **back** (rear) of the queue.
- **Deletions** are made from the **front** of the queue.
  
- The element that is first added to the queue will be the first to be removed.
---

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240410122927/FIFO-Principle-(First-In-First-Out).webp" align="right" width="300">

### FIFO Principle:

A queue operates similarly to a line of people waiting for a service, such as purchasing tickets. The first person in line is served first, and so on. This is known as the **First Come First Serve** principle. 
- **Front**: The first entry ready to be removed.
- **Rear**: The most recent entry added.

### Types of Queues:
1. **Simple Queue**: Follows the FIFO structure, allowing insertions at the rear and deletions from the front.
2. **Double-Ended Queue (Deque)**: Allows insertions and deletions from both ends. 
   - **Input Restricted Queue**: Input is allowed only at one end, but deletion can occur from either end.
   - **Output Restricted Queue**: Input can occur at both ends, but deletion is restricted to one end.
3. **Circular Queue**: The last position is connected back to the first position, with operations performed in FIFO order.
4. **Priority Queue**: Elements are accessed based on their priority.
   - **Ascending Priority Queue**: Elements are arranged in increasing order of priority.
   - **Descending Priority Queue**: Elements are arranged in decreasing order of priority.
---
### Basic Operations in Queue:
1. **Enqueue**: Adds an element to the end of the queue.
2. **Dequeue**: Removes the first element from the queue.
3. **Peek/Front**: Returns the element at the front of the queue without removing it.
4. **Rear**: Returns the element at the rear end of the queue without removing it.
5. **isFull**: Checks if the queue is full.
6. **isEmpty**: Checks if the queue is empty.


## Implementation of Queue in python:

```py

    # Implementation of Queue using Lists

    class Queue:
        def __init__(self):
            self.queue = []
        
        def enqueue(self, element):
            self.queue.append(element)
        
        def dequeue(self):
            if self.isEmpty():
                return "Queue is empty"
            return self.queue.pop(0)
        
        def peek(self):
            if self.isEmpty():
                return "Queue is empty"
            return self.queue[0]
        
        def isEmpty(self):
            return len(self.queue) == 0
        
        def size(self):
            return len(self.queue)

    # Create a queue
    myQueue = Queue()

    myQueue.enqueue('A')
    myQueue.enqueue('B')
    myQueue.enqueue('C')
    print("Queue: ", myQueue.queue)

    print("Dequeue: ", myQueue.dequeue())

    print("Peek: ", myQueue.peek())

    print("isEmpty: ", myQueue.isEmpty())

    print("Size: ", myQueue.size())
```


```python
# Implementation of Queue using Linked Lists 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, element):
        new_node = Node(element)
        if self.rear is None:
            self.front = self.rear = new_node
            self.length += 1
            return
        self.rear.next = new_node
        self.rear = new_node
        self.length += 1
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
        self.length -= 1
        if self.front is None:
            self.rear = None
        return temp.data
    
    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.front.data
    
    def isEmpty(self):
        return self.length == 0
    
    def size(self):
        return self.length

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

# Create a queue
myQueue = Queue()

myQueue.enqueue('A')
myQueue.enqueue('B')
myQueue.enqueue('C')
print("Queue: ", end="")
myQueue.printQueue()

print("Dequeue: ", myQueue.dequeue())

print("Peek: ", myQueue.peek())

print("isEmpty: ", myQueue.isEmpty())

print("Size: ", myQueue.size())
```

## Complexity Analysis:
| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Enqueue   | O(1)            | O(1)             |
| Dequeue   | O(1)            | O(1)             |
| Front     | O(1)            | O(1)             |
| Rear      | O(1)            | O(1)             |
| isEmpty   | O(1)            | O(1)             |
| isFull    | O(1)            | O(1)             |

---
### Applications of Queue:
- **Job Scheduling**: Such as printer spooling.
- **Network Devices**: Queues are used in routers/switches.
- **Algorithm Techniques**: Such as Breadth-First Search (BFS), Topological Sorting.
---
### Advantages:
- Efficient management of large data.
- Easy insertion and deletion operations due to FIFO structure.
- Suitable for scenarios with multiple consumers and single resources.
---
### Disadvantages:
- Insertion and deletion from the middle are time-consuming.
- Searching takes O(N) time.
- Maximum size needs to be predefined in array implementation.
---
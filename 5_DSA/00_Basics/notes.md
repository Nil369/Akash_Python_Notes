# 1. **Basic Terminologies**
   - **Data Structure**: A way to organize and store data in a computer so it can be used efficiently.
   - **Algorithm**: A step-by-step procedure or formula for solving a problem.
   - **Complexity**: A measure of how much time and space an algorithm takes to run.

### 2. **Types of Data Structures**
![image](https://github.com/user-attachments/assets/60daef1e-f08d-4725-b998-3d9c331b6899)

   - **Primitive Data Structures**: Basic data types like integers, floats, characters, etc.
   - **Non-Primitive Data Structures**: More complex structures that use primitive types, like:
     - **Arrays**: A collection of elements stored at contiguous memory locations.
     - **Linked Lists**: A sequence of nodes where each node points to the next one.
     - **Stacks**: A collection where elements are added/removed from the top (LIFO: Last In, First Out).
     - **Queues**: A collection where elements are added from the rear and removed from the front (FIFO: First In, First Out).
     - **Trees**: A hierarchical structure where each element has a parent and children.
     - **Graphs**: A set of vertices (nodes) connected by edges.

### 3. **Data Structure Operations**
   - **Insertion**: Adding a new element to the data structure.
     - Example: Adding a new element to an array, linked list, stack, or queue.
   - **Deletion**: Removing an element from the data structure.
     - Example: Removing an element from a stack or deleting a node in a linked list.
   - **Traversal**: Accessing each element of the data structure to process or retrieve data.
     - Example: Visiting each node in a tree or graph, or iterating through an array.

   **Example in Python:**
   ```python
   # Inserting and traversing an array
   array = [1, 2, 3, 4, 5]

   # Insertion (Add 6 at the end)
   array.append(6)

   # Traversal (Print all elements)
   for element in array:
       print(element)

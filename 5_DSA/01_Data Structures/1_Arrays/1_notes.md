## What is an Array?
An array is a `linear data structure` that stores a **collection of items of the `same data type` in `contiguous memory locations`**. Each item in an array is indexed starting with 0. We can **directly access an array element by using its index value**.

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240405101013/Memory-Representation-of-Array-(1).webp" height="400" width="800">

### Basic Terminologies of Array
- **Array Index**: In an array, elements are identified by their indexes. Array index starts from 0.
- **Array Element**: Elements are items stored in an array and can be accessed by their index.
- **Array Length**: The length of an array is determined by the number of elements it can contain.

### Memory Representation of Array
In an array, all the elements are stored in contiguous memory locations. So, if we initialize an array, the elements will be allocated sequentially in memory. This allows for efficient access and manipulation of elements.

### Importance of Array
Assume there is a class of five students and we need to keep records of their marks in an examination. We can do this by declaring five individual variables. But what if the number of students becomes very large? It would be challenging to manipulate and maintain the data.

This is where arrays become useful. Instead of using normal variables for each student, we can represent all the marks in one array, making data management much easier.

### Types of Arrays

#### Types of Arrays on the Basis of Size
1. **Fixed-Sized Arrays**:
   - The size of this array cannot be altered or updated after declaration. Here, a fixed size of memory is allocated for storage.
   - Example:
   - 
    ```python
    import array
    # Static Array
    arr = array.array('i', [1, 2, 3, 4, 5])
    print(arr)
    ```

   
2. **Dynamic-Sized Arrays**:
   - The size of the array can change as per user requirements during code execution. Python lists support dynamic-sized arrays natively.
    
    ```python
    # Dynamic Array
    arr = []
    ```

### Types of Arrays on the Basis of Dimensions

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20240731124259/Types-of-Arrays.webp">

1. **One-Dimensional Array (1-D Array)**:
   - Imagine a 1-D array as a row where elements are stored one after another.

2. **Multi-Dimensional Array**:
   - A multi-dimensional array has more than one dimension. It can be used to store complex data in the form of tables, matrices, etc.
   - **Two-Dimensional Array (2-D Array or Matrix)**: An array of arrays, structured in rows and columns.
   - **Three-Dimensional Array (3-D Array)**: An array of 2-D arrays.

### Declaration of Array
In Python, arrays (lists) can be declared in the following way:

```python
import array

# This array will store integer type elements
arr_int = array.array('i', [1, 2, 3, 4, 5])
print("Integer Array:", arr_int.tolist())

arr_char = list('abc')  # List of characters
print("Character Array:", arr_char)

# This array will store float type elements
arr_float = array.array('f', [1.0, 2.0, 3.0])
print("Float Array:", arr_float.tolist())

```

### Initialization of Array
Arrays can be initialized in different ways:

```python
arr = [1, 2, 3, 4, 5]
char_arr = ['a', 'b', 'c', 'd', 'e']
float_arr = [1.4, 2.0, 2.4, 5.0, 0.0]
```

### Operations on Array
1. **Array Traversal**: Visiting all elements of the array once.
   ```python
   arr = [1, 2, 3, 4, 5]
   # Traversing the array
   for element in arr:
       print(element)
   ```

2. **Insertion in Array**: Adding one or multiple elements at any position.
   ```python
   # Function to insert an element at a specific position
   def insert_element(arr, x, pos):
       arr.insert(pos, x)

   arr = [1, 2, 3, 5]
   insert_element(arr, 4, 3)  # Inserting 4 at position 3
   print(arr)
   ```

3. **Deletion in Array**: Removing an element at any index.
   ```python
   # Function to delete an element at a specific position
   def delete_element(arr, pos):
       if pos < len(arr):
           arr.pop(pos)

   arr = [1, 2, 3, 4, 5]
   delete_element(arr, 2)  # Deleting element at position 2
   print(arr)
   ```

4. **Searching in Array**: Traversing the array to find an element.
   ```python
   # Function to search for an element
   def find_element(arr, key):
       if key in arr:
           return arr.index(key)
       return -1  # Key not found

   arr = [1, 2, 3, 4, 5]
   index = find_element(arr, 3)  # Searching for the element 3
   print("Element found at index:", index)
   ```

## Complexity Analysis of Operations on Array

### Time Complexity:

| Operation  | Best Case | Average Case | Worst Case |
|------------|-----------|--------------|------------|
| Traversal  | Ω(N)      | θ(N)         | O(N)       |
| Insertion  | Ω(1)      | θ(N)         | O(N)       |
| Deletion   | Ω(1)      | θ(N)         | O(N)       |
| Searching  | Ω(1)      | θ(N)         | O(N)       |

### Space Complexity:

| Operation  | Best Case | Average Case | Worst Case |
|------------|-----------|--------------|------------|
| Traversal  | Ω(1)      | θ(1)         | O(1)       |
| Insertion  | Ω(1)      | θ(N)         | O(N)       |
| Deletion   | Ω(1)      | θ(N)         | O(N)       |
| Searching  | Ω(1)      | θ(1)         | O(1)       |


### Advantages of Array
- Allows random access to elements, making accessing elements by position faster.
- Better cache locality, improving performance.
- Represents multiple data items of the same type using a single name.
- Used to implement other data structures like linked lists, stacks, queues, trees, and graphs.

### Disadvantages of Array
- Fixed size: Memory cannot be increased or decreased once allocated.
- Homogeneous nature: Cannot store values of different data types.
- Contiguous memory locations make deletion and insertion difficult.

### Applications of Array
- Used in implementing other data structures like array lists, heaps, hash tables, vectors, and matrices.
- Used to store database records.
- Commonly used in lookup tables.

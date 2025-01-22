# **Analysis of an Algorithm**
   - **Goal**: To evaluate the efficiency of an algorithm in terms of time and space.
   - **Time Complexity**: How much time an algorithm takes to complete, depending on the size of the input.
   - **Space Complexity**: How much memory an algorithm uses during its execution.
   - **Best Case**: The minimum time or space an algorithm takes.
   - **Worst Case**: The maximum time or space an algorithm takes.
   - **Average Case**: The expected time or space for random input.

### **Asymptotic Notations :**  
Asymptotic notations are mathematical tools used to describe the running time of an algorithm in terms of its input size. They help in comparing the efficiency of different algorithms. 

| **Notation** | **Definition**                                             | **Example**                          |
|--------------|-----------------------------------------------------------|--------------------------------------|
| **O (Big O)**       | Represents an upper bound on the time complexity. Indicates the worst-case scenario. | \(O(n)\): A linear search in an unsorted array. |
| **Ω (Big Omega)**   | Represents a lower bound on the time complexity. Indicates the best-case scenario. | \(Ω(n)\): Finding an element in a sorted array. |
| **Θ (Big Theta)**   | Represents a tight bound on the time complexity. Indicates both upper and lower bounds. | \(Θ(n^2)\): Bubble sort in average and worst case. |

<img src="https://miro.medium.com/v2/resize:fit:1400/1*LWMGUuyLhvvSLKuaSto_hw.png">

### 1. **O(1) - Constant Time**
Accessing an element in a list by index.

```python
def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

n = 100
print(sum_of_natural_numbers(n))  # Output: 5050

```

### 2. **O(log n) - Logarithmic Time**
Binary search in a sorted array.

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(arr, 4))  # Output: 3
```

### 3. **O(n) - Linear Time**
Finding an element in an unsorted array.

```python
def find_element(arr, target):
    for element in arr:
        if element == target:
            return True
    return False

arr = [1, 4, 6, 8, 2]
print(find_element(arr, 6))  # Output: True
```

### 4. **O(n log n) - Linearithmic Time**
Merge sort implementation.

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print(arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
```

### 5. **O(n^2) - Quadratic Time**
Bubble sort implementation.

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [5, 1, 4, 2, 8]
bubble_sort(arr)
print(arr)  # Output: [1, 2, 4, 5, 8]
```

### 6. **O(2^n) - Exponential Time**
Calculating Fibonacci numbers recursively.

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))  # Output: 5
```

### 7. **O(n!) - Factorial Time**
Generating all permutations of a string.

```python
from itertools import permutations

def all_permutations(s):
    perm = [''.join(p) for p in permutations(s)]
    return perm

s = "abc"
print(all_permutations(s))  
# Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```

These examples showcase how the runtime of an algorithm increases with input size in various Big O complexities.


# **Time-Space Trade-off**
   - **Definition**: Balancing between time and space usage in an algorithm.
   - **Explanation**: Sometimes, you can make an algorithm run faster by using more memory, and vice versa.
     - **Example**: Storing precomputed results in a table (using more space) to reduce the time taken to compute them repeatedly.

   **Example:**
   - **Memoization**: Storing the results of expensive function calls to speed up subsequent calls (trading space for time).
   ```python
   # Fibonacci using memoization (time-space trade-off)
   # Dictionary to store precomputed Fibonacci values
   fib_memo = {}

   def fibonacci(n):
       if n <= 1:
           return n
       if n not in fib_memo:
           # Store the result in the memo dictionary
           fib_memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
       return fib_memo[n]

   # Initialize memoization dictionary and calculate Fibonacci of 5
   print(f"Fibonacci of 5: {fibonacci(5)}")

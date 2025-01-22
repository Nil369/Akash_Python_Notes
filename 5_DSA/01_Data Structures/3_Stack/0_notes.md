# Stack Data Structure
<img src = "https://media.geeksforgeeks.org/wp-content/uploads/20240606180735/Stack-representation-in-Data-Structures-(1).webp" height="300" align="right">

A **`stack`** is a `linear data structure` that follows the **`LIFO (Last In First Out)`** `principle`. This means that the last element inserted into the stack is the first one to be removed. The stack `allows insertion` and `deletion of elements` only `at one end`, referred to as the **`top`** of the stack.

### Key Concepts of Stack

- **LIFO Principle**: The element that is inserted last will be removed first. A real-life example is a stack of plates where the last plate added is the first one to be removed.



### Types of Stack

1. **Fixed Size Stack**: Has a predefined size. If the stack is full, an overflow error occurs when trying to add more elements.
2. **Dynamic Size Stack**: Can grow and shrink dynamically. Implemented using a linked list, allowing flexible resizing.

---
### Basic Operations on Stack

1. **push()**: Inserts an element into the stack.
2. **pop()**: Removes the top element from the stack.
3. **top()/peak()**: Returns the top element without removing it.
4. **isEmpty()**: Checks if the stack is empty.
5. **isFull()**: Checks if the stack is full.

---
### Algorithms for Stack Operations

<img src = "https://miro.medium.com/v2/resize:fit:1400/1*W2cK1baYQ5nt5vEEFgICeQ.png" height="300" align="right">

- `Push Operation`:
Append the element to the end of the list.

- `Pop Operation `:
Check if the stack is empty.
If not empty, remove and return the last element from the list.

- `Peek Operation`:
Check if the stack is empty.
If not empty, return the last element in the list.

- `isEmpty Operation`:
Return True if the list is empty, otherwise return False.

- `Size Operation`:
Return the length of the list.


## Stack Implementation

#### Using Array

In an array-based implementation, the stack uses an array to store elements. The top pointer is incremented or decremented during push and pop operations.

```py
# Python program for implementation of stack using array

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Item {item} pushed to stack.")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example Usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Top item:", stack.peek())
print("Item popped:", stack.pop())
print("Current stack size:", stack.size())
print("Is stack empty?", stack.is_empty())

```
---
#### Using Linked List

In a linked list-based implementation, each element is stored in a node, and the nodes are linked together.

```py
# C program for implementation of stack using linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_node.value

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.head.value

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

myStack = Stack()
myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Pop: ", myStack.pop())
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.stackSize())
```

## Complexity Analysis

| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| push()    | O(1)            | O(1)             |
| pop()     | O(1)            | O(1)             |
| top()     | O(1)            | O(1)             |
| isEmpty() | O(1)            | O(1)             |
| isFull()  | O(1)            | O(1)             |

### Advantages of Stack

1. **Simplicity**: Easy to implement and understand.
2. **Efficiency**: Constant time operations (O(1)) for push and pop.
3. **Memory-Efficient**: Only stores elements that are pushed.

### Disadvantages of Stack

1. **Limited Access**: Only the top element can be accessed.
2. **Overflow Risk**: Fixed-size stacks can overflow.
3. **No Random Access**: Cannot access elements randomly.

### Applications of Stack

1. **Expression Evaluation**: Conversion from infix to postfix/prefix.
2. **Function Calls**: Handling function call sequences.
3. **Memory Management**: Used in managing memory in many systems.
4. **Redo-Undo Operations**: Common in editors and browsers.
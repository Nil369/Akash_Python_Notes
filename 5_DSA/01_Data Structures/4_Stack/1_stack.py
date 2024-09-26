from collections import deque

# Stack class implementation
class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
        print(f"Item {val} pushed to stack.")

    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        else:
            return "Stack is empty!"

    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return "Stack is empty!"

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def print_stack(self):
        if not self.is_empty():
            print("Stack elements (top to bottom):")

            # Print elements from top (rightmost) to bottom (leftmost)
            for element in reversed(self.container):
                print(element)

# Function to display the menu
def menu():
    print("\n----- Stack Operations Menu -----")
    print("1. Push\n2. Pop\n3. Peek\n4. Check if stack is Empty\n5. Size\n6. Print\n7. Exit")
    print("-"*35)

# Main Program: Menu-driven stack operations
if __name__ == "__main__":
    stack = Stack()

    while True:
        menu()
        choice = input("\nEnter your choice: ")

        if choice == '1':
            val = input("Enter the value to push: ")
            stack.push(val)

        elif choice == '2':
            popped_value = stack.pop()
            print(f"Popped Value: {popped_value}")

        elif choice == '3':
            top_value = stack.peek()
            print(f"Top Value (Peek): {top_value}")

        elif choice == '4':
            if stack.is_empty():
                print("Stack is Empty.")
            else:
                print("Stack is NOT Empty.")

        elif choice == '5':
            print(f"Size of Stack: {stack.size()}")

        elif choice == '6':
            print(f"{stack.print_stack()}")

        elif choice == '7':
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")

from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        print(f"Enqueued: {val}")
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty!"
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements:")
            for elem in reversed(self.buffer):
                print(elem)

# Menu-driven program
def main():
    queue = Queue()
    while True:
        print("\nQueue Operations Menu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Check if queue is empty")
        print("4. Get queue size")
        print("5. Display all elements in the queue")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            val = input("Enter value to enqueue: ")
            queue.enqueue(val)
        
        elif choice == '2':
            dequeued_item = queue.dequeue()
            print(f"Dequeued item: {dequeued_item}")
        
        elif choice == '3':
            if queue.is_empty():
                print("Queue is empty.")
            else:
                print("Queue is not empty.")
        
        elif choice == '4':
            print(f"Queue size: {queue.size()}")
        
        elif choice == '5':
            queue.display()
        
        elif choice == '6':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, please choose a valid option.")

if __name__ == '__main__':  
    main()

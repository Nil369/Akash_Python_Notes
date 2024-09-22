class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        # Print the list in forward direction
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print("Forward: ", llstr, " --> null")

    def print_backward(self):
        # Print the list in backward direction
        if self.head is None:
            print("Linked list is empty")
            return
        # Find the last node
        itr = self.head
        while itr.next:
            itr = itr.next

        # Traverse backward
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print("Backward:", llstr, " --> null")

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        node = Node(data, None, itr)
        itr.next = node

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                if itr.next:
                    itr.next.prev = itr
                break
            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurrence of data_after value in linked list
        # Now insert data_to_insert after data_after node
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                if itr.next:
                    itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
        print(f"Value {data_after} not found in the list")

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.data == data:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        itr = self.head
        while itr:
            if itr.data == data:
                if itr.next:
                    itr.next.prev = itr.prev
                if itr.prev:
                    itr.prev.next = itr.next
                return
            itr = itr.next
        print(f"Value {data} not found in the list")


def menu():
    print("\nMenu:")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Index")
    print("4. Remove at Index")
    print("5. Get Length")
    print("6. Print List Forward")
    print("7. Print List Backward")
    print("8. Insert Multiple Values")
    print("9. Insert After Value")
    print("10. Remove By Value")
    print("0. Exit")

if __name__ == '__main__':
    dll = DoublyLinkedList()
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                data = input("Enter data to insert at beginning: ")
                dll.insert_at_beginning(data)
            case 2:
                data = input("Enter data to insert at end: ")
                dll.insert_at_end(data)
            case 3:
                index = int(input("Enter index to insert data at: "))
                data = input("Enter data to insert: ")
                try:
                    dll.insert_at(index, data)
                except Exception as e:
                    print(e)
            case 4:
                index = int(input("Enter index to remove data from: "))
                try:
                    dll.remove_at(index)
                except Exception as e:
                    print(e)
            case 5:
                print(f"Length of list: {dll.get_length()}")
            case 6:
                dll.print_forward()
            case 7:
                dll.print_backward()
            case 8:
                data_list = input("Enter values separated by space: ").split()
                dll.insert_values(data_list)
            case 9:
                data_after = input("Enter the value after which to insert: ")
                data_to_insert = input("Enter data to insert: ")
                dll.insert_after_value(data_after, data_to_insert)
            case 10:
                data = input("Enter data to remove: ")
                dll.remove_by_value(data)
            case 0:
                print("Exiting program.")
                break
            case _:
                print("Invalid choice! Please choose a valid option.")

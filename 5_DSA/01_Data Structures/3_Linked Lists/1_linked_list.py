class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print('\n'+"*"*80)
            print("Linked list is empty")
            print('\n'+"*"*80)
            return
        itr = self.head
        llstr = ''
        print('\n'+"*"*80)
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr, " --> null")
        print('\n'+"*"*80)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

def menu():
    print("\nMenu:")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Index")
    print("4. Remove at Index")
    print("5. Get Length")
    print("6. Print List")
    print("7. Insert Multiple Values")
    print("8. Exit")

if __name__ == '__main__':
    ll = LinkedList()
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        
        match choice:
            case 1:
                data = input("Enter data to insert at beginning: ")
                ll.insert_at_begining(data)
            case 2:
                data = input("Enter data to insert at end: ")
                ll.insert_at_end(data)
            case 3:
                index = int(input("Enter index to insert data at: "))
                data = input("Enter data to insert: ")
                try:
                    ll.insert_at(index, data)
                except Exception as e:
                    print(e)
            case 4:
                index = int(input("Enter index to remove data from: "))
                try:
                    ll.remove_at(index)
                except Exception as e:
                    print(e)
            case 5:
                print(f"Length of list: {ll.get_length()}")
            case 6:
                ll.print()
            case 7:
                data_list = input("Enter values separated by space: ").split()
                ll.insert_values(data_list)
            case 8:
                print("Exiting program.")
                break
            case _:
                print("Invalid choice! Please choose a valid option.")

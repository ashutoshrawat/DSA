class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if not self.head:
            # Create head for the linked list
            self.head = node
        else:
            # Link the last node and the new node
            temp = self.head
            while temp: 
                temp = temp.next
            temp.next = node

    def display(self):
        temp = self.head
        while temp:
            print("Element is:", temp.data)
            temp = temp.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.display()



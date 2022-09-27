# Node class
class Node:

    # function to initialize the node object
    def __init__(self, data):
        self.data = data # Assign data
        self.next = None # Initialize next as null

# Linked List class contains a node object
class LinkedList:
    # Function to initialize head
    # List object
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

# Code execution starts here
if __name__=='__main__':

    # Starts with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second; #Link first node with second
    second.next = third;

    llist.printList()
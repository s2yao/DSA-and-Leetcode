class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_ll(self, data):
        node = Node(data)
        # if there isnt anything in the list yet
        if not self.head:
            self.head = node
            return
        
        # iterate to find the last node in the ll
        curr = self.head
        while curr.next:
            curr = curr.next
        # ATP curr sits on last node
        curr.next = node
        return
    
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end = " -> ")
            curr = curr.next
        print("None")
        
    def insert(self, index, data):
        node = Node(data)
        if index == 0:
            node.next = self.head
            self.head = node
            return
        # traverse to find the node
        curr = self.head
        for _ in range(index - 1)
            if curr is None: return
            curr = curr.next
        # we sit on the target node
        node.next = curr.next
        curr.next = node
        return
    # Delete a node by value
    def delete(self, data):


    # Reverse the list
    def reverse(self):


        
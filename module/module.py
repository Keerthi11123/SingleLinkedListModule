class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None  # Initializing an empty list

    def append(self, val):
        """Adds a new node at the end of the list."""
        new_node = ListNode(val)
        if not self.head:  # If list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:  # Traverse to the last node
            temp = temp.next
        temp.next = new_node  # Add new node at the end

    def prepend(self, val):
        """Adds a new node at the beginning of the list."""
        new_node = ListNode(val, self.head)
        self.head = new_node  # Update head

    def delete(self, key):
        """Deletes a node with a specific value."""
        temp = self.head
        if temp and temp.val == key:
            self.head = temp.next  # Remove the head node
            return
        prev = None
        while temp and temp.val != key:
            prev = temp
            temp = temp.next
        if temp:  # If key is found
            prev.next = temp.next  # Bypass the node

    def reverse(self):
        """Reverses the linked list in-place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        """Prints the linked list."""
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

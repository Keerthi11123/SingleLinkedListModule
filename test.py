from module import LinkedList

# Create a LinkedList object and test
ll = LinkedList()
ll.append(10)
ll.prepend(5)
ll.display()
print("Original List:")
ll.display()

ll.reverse()
print("Reversed List")
ll.display()

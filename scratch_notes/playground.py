class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Initialize the next pointer to None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        """Delete the first node with the specified value."""
        if not self.head:  # If the list is empty
            return

        # If the node to be deleted is the head
        if self.head.data == data:
            self.head = self.head.next
            return

        # Find the node before the node to be deleted
        current_node = self.head
        while current_node.next and current_node.next.data != data:
            current_node = current_node.next

        # If the node was found, delete it
        if current_node.next:
            current_node.next = current_node.next.next

    def display(self):
        """Display the entire list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.display()  # Outputs: 0 -> 1 -> 2 -> 3 -> None

ll.delete_with_value(2)
ll.display()  # Outputs: 0 -> 1 -> 3 -> None

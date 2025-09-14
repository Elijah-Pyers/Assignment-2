from dataclasses import dataclass
from typing import Optional

# Create a Node class to represent each customer in the waitlist
@dataclass
class Node:
    """
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Optional[Node]): Reference to the next node.
    """
    name: str
    next: Optional["Node"] = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    """
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Optional[Node]): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    """

    def __init__(self):
        self.head: Optional[Node] = None

    def add_front(self, name: str) -> str:
        """Add a customer to the front of the waitlist."""
        new_node = Node(name=name, next=self.head)
        self.head = new_node
        return f"{name} added to the front of the waitlist"

    def add_end(self, name: str) -> str:
        """Add a customer to the end of the waitlist."""
        new_node = Node(name=name)
        if self.head is None:
            self.head = new_node
            return f"{name} added to the end of the waitlist"

        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        return f"{name} added to the end of the waitlist"

    def remove(self, name: str) -> str:
        """Remove the first customer matching 'name'."""
        if self.head is None:
            return f"{name} not found"

        # If the head is the one to remove
        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"

        # Otherwise, find the node before the one we want to remove
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.name == name:
                prev.next = curr.next
                return f"Removed {name} from the waitlist"
            prev, curr = curr, curr.next

        return f"{name} not found"

    def print_list(self) -> None:
        """Print the current waitlist, top to bottom."""
        if self.head is None:
            print("The waitlist is empty")
            return

        print("Current waitlist:")
        curr = self.head
        while curr is not None:
            print(f"- {curr.name}")
            curr = curr.next


def waitlist_generator():
    """Interface for managing the waitlist."""
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            name = input("Enter customer name to add to front: ").strip()
            if name:
                print(waitlist.add_front(name))
            else:
                print("Name cannot be empty.")

        elif choice == "2":
            name = input("Enter customer name to add to end: ").strip()
            if name:
                print(waitlist.add_end(name))
            else:
                print("Name cannot be empty.")

        elif choice == "3":
            name = input("Enter customer name to remove: ").strip()
            if name:
                print(waitlist.remove(name))
            else:
                print("Name cannot be empty.")

        elif choice == "4":
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break

        else:
            print("Invalid option. Please choose 1–5.")


if __name__ == "__main__":
    waitlist_generator()


    # ---------------------------- DESIGN MEMO ----------------------------
# How does your list work?
# This program uses a linked list where each node stores a customer's
# name and a pointer to the next node. The LinkedList class holds a reference
# to the head (first node). Adding to the front creates a new node whose next
# points to the current head, then updates the head. Adding to the end walks the
# list until the last node (whose next is None) and appends a new node there.
# Removal handles three cases: empty list, removing the head, or removing a
# node in the middle/end by relinking the previous node’s next pointer to skip
# the removed node. Printing goes from the head to None and outputs names.

# What role does the head play?
# The head is the entry point to the structure. All operations start from the head:
# traversal, insertion (front/end), and removal. Updating the head is required when
# inserting at the front or removing the first element. Without the head, access to 
# the list would be lost. Keeping head accurate is essential for correctness and 
# performance because if the head is wrong then printing and removing customers won't work.

# When might a real engineer need a custom list like this?
# Custom lists are useful when you need precise control over memory layout or
# insertion/removal complexity, when avoiding reallocation of arrays, 
# or when adding or removing from the list. In systems, networking, schedulers, 
# and internal tools, linked lists are common for data structures, event queues, 
# and free lists, when built-ins don’t provide required performance.
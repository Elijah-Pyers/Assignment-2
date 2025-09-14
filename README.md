# Waitlist Manager
You've joined the internal tools team at an event ticketing company. The support staff needs a way to manage customer waitlists when events sell out. Some customers need to be added to the front (VIPs), others go to the end (general customers), and sometimes specific customers need to be removed manually. 

Instead of relying on built-in lists or queues, you're tasked with building a custom linked list structure that gives full control over how the waitlist behaves. Your program should run in the terminal and allow users to: 
- Add customers to the front or end of the list 
- Remove customers by name 
- Print the current waitlist 

This assignment builds your understanding of singly linked lists, the role of `head` and `next`, and how to add or remove nodes from any position. These skills are foundational not just for interviews, but also for building dynamic, flexible systems. You’ll apply everything from this unit to design your own `Node` and `LinkedList` classes, handle dynamic input, and build a practical tool that mimics what real-world engineers create in internal systems.

## Classes

### `Node` Class
Represents a single unit in a singly linked list.

**Constructor**

```python
Node(name)
```

**Attributes**
- `name` (str): The name of the customer.
- `next` (Node or None): Points to the next node in the list.


### `LinkedList` Class
Manages a singly linked list of `Node` instances.

**Constructor**
```python
LinkedList()
```

**Attributes**
- `head` (Node or None): Reference to the first node in the list.

**Methods**

`add_front(name: str) -> None`
- Inserts a new node at the beginning of the list.

`add_end(name: str) -> None`
- Appends a new node to the end of the list.

`remove(name: str) -> str`
- Removes the node with the specified name. Returns a confirmation or error message.

`print_list() -> None`
- Prints the current list of names from head to tail. If empty, prints a default message.
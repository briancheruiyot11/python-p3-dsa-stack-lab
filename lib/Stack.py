class Stack:
    def __init__(self, items=None, limit=100):
        """Initialize the stack with optional items and limit"""
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        """Return True if stack is empty"""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the stack; do nothing if full"""
        if self.full():
            return  
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack, or None if empty"""
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it, or None if empty"""
        if self.isEmpty():
            return None
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack"""
        return len(self.items)

    def full(self):
        """Return True if stack is full"""
        return len(self.items) >= self.limit

    def search(self, target):
        """
        Return distance from the top of stack to target
        Top element has distance 0. Return -1 if not found.
        """
        try:
            
            index = self.items.index(target)
            return len(self.items) - 1 - index
        except ValueError:
            return -1

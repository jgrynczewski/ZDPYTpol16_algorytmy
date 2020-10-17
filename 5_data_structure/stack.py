# Stos (LIFO)
# push, pop, peak
from node import Node


class Stack:
    def __init__(self, max_size=20):
        self.top_item = None
        self.size = 0
        self.max_size = max_size

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("Out of space")

    def pop(self):
        if not self.is_empty():
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        else:
            print("Stack is empty")

    def peak(self):
        if not self.is_empty():
            return self.top_item.get_value()
        else:
            print("Stack is empty")

    def has_space(self):
        return self.size < self.max_size

    def is_empty(self):
        return self.size == 0

if __name__ == "__main__":
    s = Stack()
    s.push(34)
    s.push(22)
    s.push(11)
    s.push(10)

    print(s.peak())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

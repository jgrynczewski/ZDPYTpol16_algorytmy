# Kolejka (FIFO)
# enqueu - wkadanie
# dequeue - zdejmowanie
# peak - zwracanie wartości bez zdejmowania
from node import Node


class Queue:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0

    def enqueue(self, value):
        if self.has_space():
            item_to_add = Node(value)

            if self.is_empty():
                self.head = item_to_add
                self.tail = item_to_add
            else:
                self.tail.set_next_node(item_to_add)
                self.tail = item_to_add
            self.size += 1
        else:
            print("No more space")

    def dequeu(self):
        if not self.is_empty():
            item_to_remove = self.head

            if self.get_size() == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
                self.size -= 1
                return item_to_remove.get_value()
        else:
            print("The queue is empty.")

    def peak(self):
        if not self.is_empty():
            return self.head.get_value()
        else:
            print("The queue is empty.")

    def get_size(self):
        return self.size

    def has_space(self):
        if self.max_size is None:
            return True
        return self.max_size > self.get_size()

    def is_empty(self):
        return self.get_size() == 0

if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(23)
    q.enqueue(1)
    q.enqueue(3)

    print(q.dequeu())
    print(q.dequeu())
    print(q.dequeu())
    print(q.dequeu())
    q.dequeu()
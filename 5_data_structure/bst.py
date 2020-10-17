# Drzewo przeszukiwań binarnych
# Binary Search Tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, new_value):
        self._insert_helper(self.root, new_value)

    def _insert_helper(self, current_node, new_value):
        if current_node.value < new_value:
            if current_node.right:
                self._insert_helper(current_node.right, new_value)
            else:
                current_node.right = Node(new_value)
        if current_node.value > new_value:
            if current_node.left:
                self._insert_helper(current_node.left, new_value)
            else:
                current_node.left = Node(new_value)

    def search(self, find_value):
        return self._search_helper(self.root, find_value)

    def _search_helper(self, current_node, find_value):
        if current_node:
            if current_node.value == find_value:
                return True
            elif current_node.value > find_value:
                return self._search_helper(current_node.left, find_value)
            else:
                return self._search_helper(current_node.right, find_value)
        else:
            return False

if __name__ == "__main__":
    s = [1, 3, 4, 5, 6, 7, 89, 356]
    bst = BST(s[0])
    for item in s[1:]:
        bst.insert(item)

    print(bst.search(6))
    print(bst.search(23))
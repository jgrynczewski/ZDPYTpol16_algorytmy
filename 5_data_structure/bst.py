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

    def travers_dfs(self):
        self._travers_dfs_helper(self.root)

    def _travers_dfs_helper(self, current_node):
        # pre order dfs (NLR)
        # in order dfs (LNR)
        # post order dfs (LRN)

        if current_node:
            print(current_node.value)  # (N) - zwróć aktualny węzeł # pre-order (NLR)
            self._travers_dfs_helper(current_node.left)  # (L) - rekursywnie przejdź lewe poddrzewo
            # print(current_node.value)  # (N) - zwróć aktualny węzeł # in-order (LNR)
            self._travers_dfs_helper(current_node.right)  # (R) - reukrsywnie przejdź prawe poddrzewo
            # print(current_node.value)  # (N) - zwróć aktualny węzeł # post-order (LRN)


if __name__ == "__main__":
    s = [4, 2, 6, 1, 3, 5, 7]
    bst = BST(s[0])
    for item in s[1:]:
        bst.insert(item)

    print(bst.search(6))
    print(bst.search(23))
    print("#########")
    bst.travers_dfs()

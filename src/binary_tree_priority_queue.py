class Node:
    def __init__(self, value, priority, left=None, right=None):
        self.value = value
        self.priority = priority
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def __element_place(self, priority, node):
        if priority <= node.priority:
            if node.left:
                return self.__element_place(priority, node.left)
            else:
                return node, True
        elif priority > node.priority:
            if node.right:
                return self.__element_place(priority, node.right)
            else:
                return node, False    

    def _add_element(self, element, priority):
        if not self.root:
            self.root = Node(element, priority)
            return

        parent, is_left = self.__element_place(priority, self.root)

        if is_left:
            parent.left = Node(element, priority)
        else:
            parent.right = Node(element, priority)

    def _add_recursive(self, node, value, priority):
        if priority <= node.priority:
            if node.left is None:
                node.left = Node(value, priority)
            else:
                self._add_recursive(node.left, value, priority)
        else:
            if node.right is None:
                node.right = Node(value, priority)
            else:
                self._add_recursive(node.right, value, priority)
    
    def _find_max_node_and_parent(self, node, parent):
        if node.right is None:
            return node, parent
        return self._find_max_node_and_parent(node.right, node)

    def _remove_max_priority(self):
        if self.root is None:
            return None
        max_node, parent = self._find_max_node_and_parent(self.root, None)
        if parent is None:
            self.root = max_node.left
        else:
            parent.right = max_node.left
        return max_node.value

    def _view_queue(self, node):
        if node is None:
            return

        self._view_queue(node.right)
        print(node.priority)
        self._view_queue(node.left)

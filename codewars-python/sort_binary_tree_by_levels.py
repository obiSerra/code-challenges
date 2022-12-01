class Node:
    def __str__(self):
        v = "" if self.value is None else str(self.value)
        return f"{v} \n{self.left} {self.right}"

    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


tree_1 = Node(
    Node(None,
         Node(None, None, 4),
         2),
    Node(
        Node(None, None, 5),
        Node(None, None, 6),
        3),
    1)


def tree_by_levels(node):

    nodes = []
    queue = [node]

    while len(queue) > 0:
        current = queue.pop(0)
        if node is not None:
            nodes.append(current.value)
            queue.append(current.left)
            queue.append(current.right)

    return nodes


print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2),
      Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))

print(tree_by_levels(None))

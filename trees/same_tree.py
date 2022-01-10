# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Create tree


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def identical_trees(a, b):

    # Both empty
    if a is None and b is None:
        return True

    # Both non-empty
    if a is not None and b is not None:
        return (
            (a.data == b.data)
            and identical_trees(a.left, b.left)
            and identical_trees(a.right, b.right)
        )
    # One empty and one not
    return False


if __name__ == "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.right.right = Node(5)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(2)
    root2.right.right = Node(5)

    print(identical_trees(root1, root2))

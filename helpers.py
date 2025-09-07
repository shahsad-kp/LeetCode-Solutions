from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: 'ListNode') -> bool:
        current_self = self
        current_other = other
        while current_self and current_other:
            if current_self.val != current_other.val:
                return False
            current_self = current_self.next
            current_other = current_other.next
        return current_self is None and current_other is None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: 'TreeNode' = left
        self.right: 'TreeNode' = right

    def __repr__(self):
        return f'<{self.val}, {self.left}-{self.right}>'

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


def list_to_tree(data):
    if not data or data[0] is None:
        return None

    root = TreeNode(data[0])
    queue = deque([root])
    i = 1

    while queue and i < len(data):
        current = queue.popleft()

        if i < len(data) and data[i] is not None:
            current.left = TreeNode(data[i])
            queue.append(current.left)
        i += 1

        if i < len(data) and data[i] is not None:
            current.right = TreeNode(data[i])
            queue.append(current.right)
        i += 1

    return root
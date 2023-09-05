import loguru as logger


class TreeAlgos(object):
    def __init__(self) -> None:
        pass

    def TreeNode(self, val):
        self.root = val
        self.left = None
        self.right = None

    def BinarySearchTree(self, root, val):
        """
        This function is used to do binary search using Tree datastructure starting from a root node

        """
        curr = root
        while curr is not None:
            if val == curr.val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right

        return None

    def InsertNodeTree(self, root, val):
        """
        This function is used to do insert a val into an existing tree
        """

        new_node = self.TreeNode(val)
        if root is None:
            return new_node

        prev = None
        curr = root
        while curr is not None:
            if val == curr.val:
                logger.debug("Value already exists")
            elif val < curr.value:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right

        if val < prev.value:
            prev.left = new_node
        else:
            prev.right = new_node

        return root

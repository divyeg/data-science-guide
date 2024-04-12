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

    def DeleteNodeBST(self, root, value_list):
        """
        This function is used to delete list of nodes given root node
        """
        if root is None:
            return None

        for i in value_list:
            curr = root
            prev = None
            while curr is not None:
                if curr.value == i:
                    break
                elif curr.value < i:
                    prev = curr
                    curr = curr.right
                else:
                    prev = curr
                    curr = curr.left

            if curr is None:
                continue

            if curr.right is None and curr.left is None:  # current node is a leaf
                if prev is None:
                    root = None
                elif curr is prev.left:
                    prev.left = None
                else:
                    prev.right = None

            elif curr.right is None and curr.left is not None:
                if prev is None:
                    root = curr.left
                elif curr is prev.left:
                    prev.left = curr.left
                else:
                    prev.right = curr.left

            elif curr.right is not None and curr.left is None:
                if prev is None:
                    root = curr.right
                elif curr is prev.left:
                    prev.left = curr.right
                else:
                    prev.right = curr.right
            else:
                # find successor
                succ = curr.right
                curr_temp = curr.right
                while curr_temp.left is not None:
                    curr_temp = curr_temp.left
                    succ = curr_temp

                self.DeleteNodeBST(root, [succ.value])

                if prev is None:
                    root.value = succ.value
                elif curr is prev.left:
                    prev.left.value = succ.value
                else:
                    prev.right.value = succ.value

        return root

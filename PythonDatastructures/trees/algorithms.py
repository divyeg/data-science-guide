import loguru as logger


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class TreeAlgos(object):
    def __init__(self) -> None:
        pass

    def ConstructBinaryTree(self, vals):
        """
        This function is used to create a binary tree from list of values
        """
        n = len(vals)
        if n == 0:
            return None

        root = TreeNode(vals[0])
        node_stack = [root]
        i = 1

        while i < n:
            curr = node_stack.pop(0)
            if i < n:
                curr.left = TreeNode(vals[i])
                node_stack.append(curr.left)
                i += 1
            if i < n:
                curr.right = TreeNode(vals[i])
                node_stack.append(curr.right)
                i += 1
        return root

    def PrintTree(self, root):
        if root is None:
            return None

        self.PrintTree(root.left)
        print(root.val, end=" ")
        self.PrintTree(root.right)

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

    def MeasureTreeHeight(self, root):
        """
        Args:
        root(BinaryTreeNode_int32)
        Returns:
        int32
        """
        # level order traversal
        if root is None:
            return 0
        height = 0
        q = []

        q.append(root)

        while q:
            height += 1

            for i in range(len(q)):
                node = q.pop(0)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

        return height

    def CheckIfBST(root):
        """
        Args:
        root(BinaryTreeNode_int32)
        Returns:
        bool
        """
        # if a tree is BST, then all the elements in inorder traversal should be sorted
        node = root
        node_stack = []
        prev_value = None

        while node or node_stack:
            while node:
                node_stack.append(node)
                node = node.left

            node = node_stack.pop()
            if prev_value and prev_value > node.value:
                return False

            prev_value = node.value
            node = node.right
        return True

    def PrintAllPaths(root):
        """
        Args:
        root(BinaryTreeNode_int32)
        Returns:
        list_list_int32
        """

        def helper(root, path, path_list):
            path.append(root.val)

            if root.left is None and root.right is None:
                path_list.append(path.copy())

            else:
                if root.left is not None:
                    helper(root.left, path, path_list)

                if root.right is not None:
                    helper(root.right, path, path_list)
            path.pop()

        path = []
        path_list = []
        helper(root, path, path_list)

        return path_list


tree_object = TreeAlgos()
val_list = [1, 2, 3, 4, 5, 6, 7]
root = tree_object.ConstructBinaryTree(val_list)

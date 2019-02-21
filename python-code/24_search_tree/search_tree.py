from collections import deque


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.value)


class SearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        如果要插入数据比节点数据大，并且节点的右子树为空，直接将数据插入到右子节点位置，否则，递归遍历右子树；
        如果要插入数据比节点数据小，并且节点的左子树为空，直接将数据插入到左子节点，否则，递归遍历左子树
        """
        if self.root is None:
            self.root = TreeNode(value)
            return

        p = self.root
        while p is not None:
            if value > p.value:
                if p.right is None:
                    p.right = TreeNode(value)
                    return
                p = p.right
            elif value < p.value:
                if p.left is None:
                    p.left = TreeNode(value)
                    return
                p = p.left

    def find(self, value):
        """
        先取根节点，如果要查找的数据比根节点小，那么在左子树中递归查找；
        如果要查找数据比根节点大，那么在右子树中查找
        """
        if self.root is None:
            return None

        p = self.root
        while p is not None:
            if value < p.value:
                p = p.left
            elif value > p.value:
                p = p.right
            else:
                return p
        return None

    def delete(self, value):
        """
        1. 寻找这个节点，记录节点和他的父节点
        2. 如果有两个子节点，遍历右子树，找到最小值节点，
           用最小值节点替换掉该节点（父节点指向最小值节点），删除最小值节点（最小值节点父节点指向 None）
        3. 如果只有一个子节点，更新父节点指针，指向这一个子节点
        4. 如果没有子节点，直接将父节点指针指向 None
        """
        p = self.root
        parent = None
        # 寻找要删除的节点
        while p is not None and p.value != value:
            parent = p
            if value > p.value:
                p = p.right
            elif value < p.value:
                p = p.left

        # 没有找到要删除的节点
        if p is None:
            return None
        # 删除根节点
        if parent is None:
            self.root = None
            return

        # 左子节点和右子节点都有, 遍历右子树中的最小值节点
        if p.left and p.right:
            minp = p.right
            minparent = p  # 最小值节点的父节点
            while minp.left is not None:
                minparent = minp
                minp = minp.left
            p.value = minp.value
            # parent 与 p 与前面查找的结果统一，避免重复代码
            parent = minparent
            # 最小值节点是没有左节点
            p = minp

        # 找到 p 的子节点
        # 只有左子节点
        if p.left is not None:
            child = p.left
        # 只有右子节点
        elif p.right is not None:
            child = p.right
        else:
            child = None  # 删除叶节点

        if parent.left == p:
            parent.left = child
        else:
            parent.right = child

    # 中序遍历顺序打印树
    def in_order(self, root):
        if root:
            yield from self.in_order(root.left)
            yield root.value
            yield from self.in_order(root.right)

    # 层遍历
    def level_order(self):
        level = 1
        if self.root:
            node_deque = deque([(self.root, level)])
        else:
            node_deque = None

        while node_deque and len(node_deque) > 0:
            tmp, l = node_deque.popleft()
            yield str(tmp.value), l
            level = l + 1
            if tmp.left:
                node_deque.append((tmp.left, level))
            if tmp.right:
                node_deque.append((tmp.right, level))

    @property
    def level(self):
        level = 1
        for n, l in self.level_order():
            level = max(level, l)
        return '二叉树高度：' + str(level)

    def tree_string(self):
        pre_lv = None
        tree_str = ''
        for n, l in self.level_order():
            if pre_lv != l:
                tree_str += '\n' + n
            else:
                tree_str += '\t' + n
            pre_lv = l
        return tree_str.strip()

    def __repr__(self):
        return self.tree_string()


if __name__ == '__main__':
    nums = [33, 16, 50, 13, 18, 34, 58, 17, 15, 25, 51, 66, 19, 27, 55, 26, 36]
    stree = SearchTree()
    for i in nums:
        stree.insert(i)
    print(list(stree.level_order()))
    print(stree)
    print(list(stree.in_order(stree.root)))

    n = stree.find(27)
    print(n.left, n.right)

    print(stree.delete(18))
    print(stree)
    print(stree.level)
    # 删除根节点
    print(stree.delete(33))
    print(stree)

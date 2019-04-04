from collections import deque


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 前序遍历，值，左子树，右子树
def pre_order(root):
    if root:
        yield root.value
        yield from pre_order(root.left)
        yield from pre_order(root.right)


# 中序遍历，左子树，值，右子树
def in_order(root):
    if root:
        yield from in_order(root.left)
        yield root.value
        yield from in_order(root.right)


# 后序遍历，左子树，右子树，值
def post_order(root):
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.value


# 层遍历
def level_order(root):
    """
    按层遍历，实际上是广度优先算法，借助队列来做。
    """
    if root:
        level = 1
        node_deque = deque([(root, level)])
        while len(node_deque) > 0:
            tmp, l = node_deque.popleft()
            yield tmp.value, l
            level = l + 1
            if tmp.left:
                node_deque.append((tmp.left, level))
            if tmp.right:
                node_deque.append((tmp.right, level))
    else:
        yield None, 0


def tree_height(node):
    """
    返回二叉树高度
    :param node:
    :return:
    """
    if node is None:
        return 0
    hleft = tree_height(node.left)
    hright = tree_height(node.right)
    return max(hleft, hright) + 1


if __name__ == '__main__':
    root = TreeNode('A')
    first_B = TreeNode('B')
    first_C = TreeNode('C')
    sec_D = TreeNode('D')
    sec_E = TreeNode('E')
    sec_F = TreeNode('F')
    root.left, root.right = first_B, first_C
    first_B.left, first_B.right = sec_D, sec_E
    first_C.left, = sec_F,

    print(list(pre_order(root)))
    print(list(in_order(root)))
    print(list(post_order(root)))
    print(list(level_order(root)))
    print(tree_height(root))

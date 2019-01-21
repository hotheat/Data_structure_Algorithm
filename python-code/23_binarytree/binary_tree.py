from collections import deque


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 前序遍历，值，左节点，右节点
def pre_order(root):
    if root:
        yield root.value
        yield from pre_order(root.left)
        yield from pre_order(root.right)


# 中序遍历，左节点，值，右节点
def in_order(root):
    if root:
        yield from in_order(root.left)
        yield root.value
        yield from in_order(root.right)


# 后序遍历，
def post_order(root):
    if root:
        yield from post_order(root.left)
        yield from post_order(root.right)
        yield root.value


# 层遍历
def level_order(root):
    level = 1
    if root:
        node_deque = deque([(root, level)])
    while len(node_deque) > 0:
        tmp, l = node_deque.popleft()
        yield tmp.value, l
        level += 1
        if tmp.left:
            node_deque.append((tmp.left, level))
        if tmp.right:
            node_deque.append((tmp.right, level))


if __name__ == '__main__':
    root = TreeNode('A')
    first_B = TreeNode('B')
    first_C = TreeNode('C')
    sec_D = TreeNode('D')
    sec_E = TreeNode('E')
    sec_F = TreeNode('F')
    sec_G = TreeNode('G')
    root.left, root.right = first_B, first_C
    first_B.left, first_B.right = sec_D, sec_E
    first_C.left, first_C.right = sec_F, sec_G

    print(list(pre_order(root)))
    print(list(in_order(root)))
    print(list(post_order(root)))
    print(list(level_order(root)))

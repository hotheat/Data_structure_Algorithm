class Node(object):
    def __init__(self, data, _next=None):
        self.data = data
        self._next = None

    def __repr__(self):
        return self.data


class LinkedStack(object):
    def __init__(self):
        self._head = None

    def push(self, value):
        node = Node(value)
        self._push_node(node)

    def _push_node(self, node):
        node._next = self._head
        self._head = node

    def pop(self):
        node = self._head
        return self._pop_node(node)

    def _pop_node(self, node):
        if node:
            tmp = node._next
            self._head = tmp
            return node.data
        else:
            return None

    def __repr__(self):
        nums = []
        cur = self._head
        while cur:
            nums.append(str(cur.data))
            cur = cur._next
        if len(nums) > 0:
            return '->'.join(nums)
        else:
            return ''


if __name__ == '__main__':
    sl = LinkedStack()
    for i in range(8):
        sl.push(i)
    print(sl)
    for i in range(9):
        print(sl.pop())

"""
1. insertion, deletion, search of the linked-list
2. assume data type
"""

from typing import Optional


class Node(object):
    def __init__(self, data: int, next_node=None):
        self.data = data
        self._next = next_node

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __lt__(self, other):
        return self.data < other.data


class SingleLinkedList(object):

    def __init__(self):
        self._head = None

    def insert_value_to_head(self, value):
        new_node = Node(value)
        return self.insert_node_to_head(new_node)

    def insert_node_to_head(self, new_node: Node):
        if new_node:
            new_node._next = self._head
            self._head = new_node

    def insert_value_after(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_after(self, node, new_node):
        if not node or not new_node:
            return
        new_node._next = node._next
        node._next = new_node

    def find_by_value(self, value: int) -> Optional[Node]:
        # Optional 返回值 Node 或者 None
        n = self._head
        while n and n.data != value:
            n = n._next
        return n

    def find_by_index(self, index: int):
        pos = 0
        n = self._head
        while n and pos != index:
            n = n._next
            pos += 1
        return n

    def insert_value_before(self, node, value: int):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def insert_node_before(self, node, new_node):
        if not self._head or not node or not new_node:
            return
        n = self._head
        if n == node:
            self.insert_node_to_head(new_node)
            return

        while n._next and n._next != node:
            n = n._next

        new_node._next = n._next
        n._next = new_node

    def delete_by_value(self, value: int):
        if not self._head:
            return
        # 哨兵节点
        fake_head = Node(value + 1)
        fake_head._next = self._head

        prev, current = fake_head, self._head

        while current._next:
            if current.data != value:
                prev = current
                current = current._next
            else:
                prev._next = current._next
                current = current._next

        # 最后一个节点是否删除
        if current.data == value:
            prev._next = None
        # 判断第一个节点是否删除
        self._head = fake_head._next

    def reverse(self):
        if self._head is None or self._head._next is None:
            return
        # 哨兵节点为 None
        fake_head = None
        prev, cur = fake_head, self._head
        while cur:
            tmp = cur._next
            cur._next = prev
            prev, cur = cur, tmp
        # 处理头部
        self._head = prev

    def delete_last_N(self, value: int):
        """
        设置两个指针，快指针和慢指针。快指针先走 n 步，然后同时出发，
        快指针到达末尾时慢指针的位置即倒数第 n 个节点。
        """
        fast, slow = self._head, self._head
        pos = 0
        while pos < value:
            fast = fast._next
            pos += 1

        while fast._next:
            tmp = slow
            fast, slow = fast._next, slow._next

        tmp._next = slow._next

    def find_mid_node(self) -> Optional[Node]:
        """
        设置快指针和慢指针，快指针走两步，慢指针走一步，快指针到达链表尾部，停止
        """
        fast, slow = self._head, self._head
        while fast and fast._next:
            slow = slow._next
            fast = fast._next._next
        return slow

    def has_ring(self):
        """
        设置快慢两个指针，快指针每次跨两步，慢指针每次跨一步，如果没环，快指针则会顺利到达尾部
        """
        fast, slow = self._head, self._head

        while fast._next:
            fast, slow = fast._next, slow._next
            if fast._next:
                fast = fast._next
            else:
                return False
            if slow == fast:
                return True
        return False

    def merge(self, link):
        res = SingleLinkedList()
        fir, sec = self._head, link._head

        while fir and sec:
            if fir < sec:
                res.insert_value_to_head(fir.data)
                fir = fir._next
            else:
                res.insert_value_to_head(sec.data)
                sec = sec._next

        while fir:
            res.insert_value_to_head(fir.data)
            fir = fir._next

        while sec:
            res.insert_value_to_head(sec.data)
            sec = sec._next

        return res

    def __repr__(self):
        nodes = []
        current = self._head

        while current:
            nodes.append(current.data)
            current = current._next

        if len(nodes) > 0:
            return '->'.join((str(n) for n in nodes))
        else:
            return ''


if __name__ == '__main__':
    sl = SingleLinkedList()
    for i in range(5):
        sl.insert_value_to_head(i)
    print(sl)

    nodev3 = sl.find_by_value(3)
    print(nodev3)

    nodeid3 = sl.find_by_index(3)
    print(nodeid3)

    sl.insert_value_after(nodev3, 8)

    print('insert after', sl)

    sl.insert_value_before(nodev3, 18)
    print('insert before', sl)
    node0 = sl.find_by_value(0)
    sl.insert_value_before(node0, 100)
    print('insert before last node', sl)

    nodefir = sl.find_by_index(0)
    sl.insert_value_before(nodefir, 1)
    print('insert head before', sl)

    sl.delete_by_value(1)
    sl.delete_by_value(0)
    print('delete value', sl)

    sl.reverse()
    print('reversed', sl)

    sl.delete_last_N(2)
    print('deleta last n', sl)

    midn = sl.find_mid_node()
    print('middle node', midn)

    node = sl.find_by_index(0)
    sl.insert_value_after(node, 5)
    print('linked list', sl)
    midn = sl.find_mid_node()
    print('middle node', midn)

    sl.delete_by_value(4)
    print('link1', sl)
    link2 = SingleLinkedList()
    for i in [5, 4, 1]:
        link2.insert_value_to_head(i)
    print('link2', link2)

    merged = sl.merge(link2)
    print('merged', merged)

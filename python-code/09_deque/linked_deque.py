class Node(object):
    def __init__(self, value, _next=None):
        self.data = value
        self._next = None

    def __repr__(self):
        return str(self.data)


class LinkedQueue(object):
    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, value):
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail._next = node
            self._tail = node

    def dequeue(self):
        if not self._head is None:
            value = self._head.data
            self._head = self._head._next
        # 链表为空时，tail 设为 None
            if self._head is None:
                self._tail = None
        return value

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
    lq = LinkedQueue()
    for i in range(5):
        lq.enqueue(i)

    print(lq)

    for i in range(5):
        print(lq.dequeue())

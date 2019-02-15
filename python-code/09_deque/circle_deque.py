from itertools import chain


class CircularQueue(object):
    def __init__(self, n):
        # 数组含有 n 个元素，所以 self.capacity 需要加 1
        self.capacity = n + 1
        self.items = [True] * self.capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, value):
        # 判断队满
        if (self._tail + 1) % self.capacity == self._head:
            return False
        self.items[self._tail] = value
        self._tail = (self._tail + 1) % self.capacity

    def dequeue(self):
        if self._head != self._tail:
            item = self.items[self._head]
            self._head = (self._head + 1) % self.capacity
            return item

    def __repr__(self):
        if self._head < self._tail:
            return ' '.join((str(i) for i in self.items[self._head:self._tail]))
        elif self._head > self._tail:
            return ' '.join(str(i) for i in chain(self.items[self._head:], self.items[:self._tail]))
        else:
            return ''


if __name__ == '__main__':
    ara = CircularQueue(8)
    for i in range(8):
        ara.enqueue(i)
    print(ara.items)
    print(ara.dequeue())
    print(ara.dequeue())
    print(ara.dequeue())
    print(ara._head, ara._tail, ara.items)
    print('after dequeue', ara._head, ara._tail, ara)
    for i in [20, 21, 22]:
        ara.enqueue(i)
        print(ara)
        print('head', ara._head, 'tail', ara._tail)

    for i in range(8):
        print(ara.dequeue())
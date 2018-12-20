class ArrayQueue(object):
    def __init__(self, n):
        self.capacity = n
        self.items = [True] * self.capacity
        self.head = 0
        self.tail = 0

    def enqueue(self, value):
        if self.tail == self.capacity:
            if self.head == 0:
                return False
            # 搬移数据
            self.items[:self.tail - self.head] = self.items[self.head:self.tail]
            self.tail = self.tail - self.head
            self.head = 0

        self.items[self.tail] = value
        self.tail += 1

    def dequeue(self):
        "出队时注意判断队列是否为空"
        if self.head != self.tail:
            tmp = self.items[self.head]
            self.head += 1
            return tmp

    def __repr__(self):
        """
        :return: str
        """
        return ' '.join((str(i) for i in self.items[self.head:self.tail]))


if __name__ == '__main__':
    ara = ArrayQueue(10)
    for i in range(8):
        ara.enqueue(i)
    print(ara)

    print(ara.dequeue())
    print(ara.dequeue())
    print(ara.dequeue())
    print('after dequeue', ara.head, ara.tail)

    for i in [20, 21, 22]:
        print('head', ara.head, 'tail', ara.tail)
        ara.enqueue(i)

    print(ara)

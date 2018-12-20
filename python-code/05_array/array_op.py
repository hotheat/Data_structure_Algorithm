class Array(object):

    def __init__(self, capcity):
        self._data = []
        self.count = 0
        self.capcity = capcity

    def __getitem__(self, item):
        return f'index {item}', self._data[item]

    def find(self, index):
        if index >= self.count or index <= -self.count:
            return None
        return self._data[index]

    def insert(self, index: int, value: int) -> bool:
        if index >= self.capcity:
            return False

        if index < 0:
            self._data.insert(0, value)
        elif index >= self.count:
            self._data.append(value)
        else:
            self._data[index + 1:] = self._data[index:-1]
        self._data[index] = value
        self.count += 1

        return True

    def delete(self, index: int) -> bool:
        if index >= self.count or index <= -self.count:
            return False
        self._data[index:-1] = self._data[index + 1:]
        self.count -= 1
        self._data = self._data[0:self.count]
        return True

    def __repr__(self) -> str:
        return " ".join(str(num) for num in self._data[:self.count])

    def print_all(self):
        for num in self._data[:self.count]:
            print(f'{num}', num, end=' ')
        print("\n", flush=True)


def test_array():
    array = Array(3)
    for i in range(3):
        array.insert(i, i + 10)
    print('array.............', array)
    print('array item', array[1])
    array.delete(1)
    print('array delete', array)


if __name__ == '__main__':
    test_array()

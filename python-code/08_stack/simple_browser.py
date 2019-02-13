"""
浏览器三个操作：
点击新页面，前进，后退。
用两个栈 a 和栈 b。栈 a 存储可以后退的页面，栈 b 存储可以前进的页面，栈 a 为空时，没有页面可以后退。栈 b 为空时，则没有页面可以前进。
点击新页面时，将页面压入栈 a，如果栈 b 不为空，则清空，没法点击前进。
点击前进按钮，从栈 a 栈顶弹出，压入栈 b；
点击后退按钮，从栈 b 栈顶弹出，压入栈 a。
"""
import sys

sys.path.append('linked_stack.py')
from linked_stack import LinkedStack


class NewLinkedStack(LinkedStack):

    def is_empty(self):
        return not self._head


class Browser(object):
    def __init__(self):
        self.backward_stack = NewLinkedStack()
        self.forward_stack = NewLinkedStack()

    def clear_forward_stack(self):
        if not self.forward_stack.is_empty():
            self.forward_stack._head = None

    def open(self, url):
        print(f'Open url {url}')
        self.backward_stack.push(url)
        self.clear_forward_stack()

    def can_ward(self, stack):
        return not stack.is_empty()

    def forward(self):
        if self.can_ward(self.forward_stack):
            top = self.forward_stack.pop()
            self.backward_stack.push(top)
            cur_page = self.backward_stack._head
            print(f'Now you are in Page {cur_page}')
        else:
            print('No page can forward')

    def backward(self):
        if self.can_ward(self.backward_stack):
            top = self.backward_stack.pop()
            self.forward_stack.push(top)
            cur_page = self.backward_stack._head
            print(f'Now you are in Page {cur_page}')
        else:
            print('No page can forward')


if __name__ == "__main__":
    b = Browser()
    url = ['X', 'Y', 'Z']

    for i in url:
        b.open(i)

    print(b.backward_stack)

    b.backward()
    print(b.backward_stack)
    print(b.forward_stack)

    b.open('AA')
    b.forward()
    b.backward()

    b.forward()

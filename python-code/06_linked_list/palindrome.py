from Single_Linked_List import SingleLinkedList


def reverse(node):
    fake_node = None
    pre, cur = fake_node, node
    while cur:
        tmp = cur._next
        cur._next = pre
        pre, cur = cur, tmp
    return pre


def ispalindrome(linklist):
    mid_node = linklist.find_mid_node()
    last_node = reverse(mid_node)

    fir, last = linklist._head, last_node

    while fir and last:
        if fir.data != last.data:
            return False
        else:
            fir, last = fir._next, last._next
    return True


if __name__ == '__main__':
    s = 'abba'
    sl = SingleLinkedList()
    for i in s:
        sl.insert_value_to_head(i)
    print(ispalindrome(sl))

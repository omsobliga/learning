def f(head):
    pre_node = None
    node = head
    while node:
        next_node = node.next
        node.next = pre_node
        pre_node = node
        node = next_node
    return pre_node

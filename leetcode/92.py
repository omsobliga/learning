def f(head, left, right):
    count = 1
    pre_node = None
    node = head
    while count < left:
        pre_node = node
        node = node.next
        count += 1
    pre_start_node = pre_node
    start_node = node

    while node and count <= right:
        next_node = node.next
        node.next = pre_node
        pre_node = node
        node = next_node
        count += 1
    end_node = pre_node
    end_node_next = node

    if pre_start_node:
        pre_start_node.next = pre_node
    else:
        head = end_node
    start_node.next = end_node_next
    return head

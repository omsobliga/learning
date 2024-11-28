def merge_link(node1, node2):
    head = node = ListNode(None)
    while node1 or node2:
        if node1 and node2:
            if node1.val < node2.val:
                node.next = node1
                node = node1
                node1 = node1.next
            else:
                node.next = node2
                node = node2
                node2 = node2.next
        elif node1:
            node.next = node1
            node = node1
            node1 = node1.next
        else:
            node.next = node2
            node = node2
            node2 = node2.next
    return head.next


def f(lists):
    if len(lists) == 0:
        return None

    merged_node = lists[0]
    for i in range(1, len(lists)):
        node = lists[i]
        merged_node = merge_link(merged_node, node)

    return merged_node

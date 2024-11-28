def f(head):
    if not head:
        return
    if not head.next:
        return head
    pre_node = head
    cur = head.next
    while cur:
        if cur.val == pre_node.val:
            pre_node.next = cur.next
        else:
            pre_node = cur
        cur = cur.next
    return head

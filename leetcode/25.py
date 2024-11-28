def f(head, k):
    if not head:
        return None
    if k <= 0:
        return head

    cur = head
    pre_node = None
    while cur:
        pre_start_node = pre_node
        start_node = cur
        tmp = start_node
        end = False
        for i in range(k):
            if not tmp:
                end = True
                break
            else:
                tmp = tmp.next
        if end:
            break
        for i in range(k):
            next_node = cur.next
            cur.next = pre_node
            print(cur.val, "next", pre_node.val if pre_node else None)
            pre_node = cur
            cur = next_node
        end_node = pre_node
        start_node.next = next_node
        pre_node = start_node
        print("start_node", start_node.val, "next", next_node.val if next_node else None)
        if pre_start_node:
            pre_start_node.next = end_node
            print("pre_start_node", pre_start_node.val, "next", end_node.val if end_node else None)
        else:
            head = end_node
    return head

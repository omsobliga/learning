def f(head):
    cur = head
    new_head = None
    node_mapping = {}

    while cur:
        copy_node = Node(cur.val, cur.next, cur.random)
        node_mapping[cur] = copy_node
        cur = cur.next
        if new_head is None:
            new_head = copy_node

    cur = new_head
    while cur:
        cur.next = node_mapping[cur.next] if cur.next else None
        cur.random = node_mapping[cur.random] if cur.random else None
        cur = cur.next

    return new_head



def f(head):
    if not head:
        return False
    if not head.next:
        return False

    pos1 = head
    pos2 = head
    while pos1 and pos2 and pos2.next:
        pos1 = pos1.next
        pos2 = pos2.next.next
        if pos1 == pos2:
            return True
    return False

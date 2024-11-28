
def f(head):
    if not head:
        return None
    if not head.next:
        return None

    pos1 = head
    pos2 = head
    mix_pos = None

    while pos1 and pos2 and pos2.next:
        pos1 = pos1.next
        pos2 = pos2.next.next
        if pos1 == pos2:
            mix_pos = pos1
            break

    if not mix_pos:
        return None

    pos3 = head
    pos4 = mix_pos
    while pos3 != pos4:
        pos3 = pos3.next
        pos4 = pos4.next
    return pos3

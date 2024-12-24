
def s_cantain_t(s_char_count, t_char_count):
    for k, v in t_char_count.items():
        if s_char_count.get(k, 0) < v:
            return False
    return True


def f(s, t):
    t_char_count = {}
    s_char_count = {}
    for c in t:
        t_char_count[c] = t_char_count.get(c, 0) + 1

    left = 0
    right = 0
    min_window = ""
    while left <= right and right < len(s):
        c = s[right]
        while not s_cantain_t(s_char_count, t_char_count):
            s_char_count[c] = s_char_count.get(c, 0) + 1
            right += 1
            if right >= len(s):
                break
            c = s[right]

        c = s[left]
        while s_cantain_t(s_char_count, t_char_count):
            # print(s_char_count, t_char_count, s_cantain_t(s_char_count, t_char_count))
            if s_cantain_t(s_char_count, t_char_count):
                if not min_window or right - left < len(min_window):
                    min_window = s[left: right]
            s_char_count[c] -= 1
            left += 1
            if left >= len(s):
                break
            c = s[left]

    return min_window



# print(f("ADOBECODEBANC", "ABC"))
# print(f("A", "A"))
# print(f("A", "AA"))
print(f("ab", "b"))


def contain(s_count, t_count):
    for k, t_c in t_count.items():
        if s_count.get(k, 0) < t_c:
            return False
    return True


def f(s, t):
    left = 0
    right = 0

    t_count = {}
    for i in t:
        t_count[i] = t_count.get(i, 0) + 1

    min_str_length = len(s) + 1
    result = ""

    s_count = {}
    while right < len(s) or contain(s_count, t_count):
        # print(s_count, t_count, contain(s_count, t_count), left, right)
        if not contain(s_count, t_count):
            s_char = s[right]
            s_count[s_char] = s_count.get(s_char, 0) + 1
            right += 1
        else:
            # print(min_str_length, right - left)
            if min_str_length > right - left:
                min_str_length = right - left
                result = s[left: right]
            s_char = s[left]
            s_count[s_char] -= 1
            left += 1
    return result


print(f("ADOBECODEBANC", "ABC"))
print(f("a", "a"))
print(f("a", "aa"))

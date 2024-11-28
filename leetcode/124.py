
def dfs(root):
    if not root:
        return 0, None

    sum_ = root.val
    left_sum, max_left_sum = dfs(root.left)
    right_sum, max_right_sum = dfs(root.right)

    sum_ = max(sum_, sum_ + max(left_sum, right_sum))

    max_sum = root.val + max(left_sum, 0) + max(right_sum, 0)
    if max_left_sum is not None:
        max_sum = max(max_left_sum, max_sum)
    if max_right_sum is not None:
        max_sum = max(max_right_sum, max_sum)
    return sum_, max_sum


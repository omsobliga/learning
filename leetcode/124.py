

class T:

    result = None

    def max_path_sum(self, root):
        if not root:
            return 0
        left = self.max_path_sum(root.left)
        right = self.max_path_sum(root.right)

        max_value = max(root.val + max(left, 0) + max(right, 0))
        if self.result is None or self.result < max_value:
            self.result = max_value

        return max(root.val + max(left, 0), root.val + max(right, 0))



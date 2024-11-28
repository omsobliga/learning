# 前序遍历：root, left, right
# 中序遍历：left, root, right

def f(preorder, inorder):
    if not preorder:
        return None

    val = preorder[0]
    i = 0
    while True:
        if inorder[i] == val:
            break
        else:
            i += 1

    left_tree = f(preorder[1:i + 1], inorder[:i])
    right_tree = f(preorder[i+1:], inorder[i+1:])
    root = TreeNode(preorder[0], left_tree, right_tree)
    return root


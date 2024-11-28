def dfs(root, p, path, result):
    if root is None:
        return

    path.append(root)

    if root == p:
        result.append(path[:])
        # print([r.val for r in result[0]])
        return

    dfs(root.left, p, path, result)
    dfs(root.right, p, path, result)
    path.pop()


def f(root, p, q):
    path = []
    result = []
    dfs(root, p, path, result)
    p_path = result[0]
    # print([r.val for r in p_path])

    path = []
    result = []
    dfs(root, q, path, result)
    q_path = result[0]
    # print([r.val for r in q_path])

    i, j = 0, 0
    common_parent = None
    while i < len(p_path) and j < len(q_path):
        p_node = p_path[i]
        q_node = q_path[j]
        # print(p_node.val, q_node.val)
        if p_node == q_node:
            common_parent = p_node
        else:
            break
        i += 1
        j += 1
    return common_parent


def dfs(node, p, path):
    if not node:
        return
    if node == p:
        path.append(node)
        return path[:]

    path.append(node)
    res1 = dfs(node.left, p, path)
    res2 = dfs(node.right, p, path)
    path.pop()
    return res1 or res2


def f(root, p, q):
    path_p = dfs(root, p, [])
    path_q = dfs(root, q, [])
    result = None
    for i in range(min(len(path_p), len(path_q))):
        if path_p[i] == path_q[i]:
            result = path_p[i]
            continue
        else:
            break
    return result

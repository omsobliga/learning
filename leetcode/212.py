# trie + 回溯

class Node:

    def __init__(self, is_word):
        self.is_word = is_word
        self.sub_tree = {}


    def __str__(self):
        return f"is_word {self.is_word}, sub_tree {self.sub_tree.keys()}"


class Trie:

    def __init__(self):
        self.root = Node(False)

    def push(self, word):
        root = self.root
        for i, c in enumerate(word):
            is_word = i == len(word) - 1
            if c in root.sub_tree:
                root = root.sub_tree[c]
                if is_word:
                    root.is_word = 1
            else:
                node = Node(is_word)
                root.sub_tree[c] = node
                root = node


def backtracking(board, used, node, i, j, path, find_words):
    if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
        return

    # print(node.sub_tree.keys(), used, i, j, path, find_words)
    if used[i][j] == 1:
        return

    c = board[i][j]
    if c not in node.sub_tree:
        return

    used[i][j] = 1
    path.append(c)
    node = node.sub_tree[c]
    if node.is_word:
        # print(path)
        find_words.append("".join(path))
    backtracking(board, used, node, i-1, j, path, find_words)
    backtracking(board, used, node, i+1, j, path, find_words)
    backtracking(board, used, node, i, j-1, path, find_words)
    backtracking(board, used, node, i, j+1, path, find_words)
    path.pop()
    used[i][j] = 0


def f(board, words):
    if not board:
        return []

    trie = Trie()
    for word in words:
        trie.push(word)

    # print(trie.root.sub_tree)
    # print(trie.root.sub_tree["a"])

    m = len(board)
    n = len(board[0])
    result = []
    for i in range(m):
        for j in range(n):
            find_words = []
            path = []
            used = [[0] * n for _ in range(m)]
            backtracking(board, used, trie.root, i, j, path, find_words)
            result.extend(find_words)
    return list(set(result))


# print(f([["a", "a"]], ["aaa"]))
# print(f([["a", "b"], ["b", "a"]], ["abab"]))
# print(f([["a","b"],["a","a"]], ["aba","baa","bab","aaab","aaa","aaaa","aaba"]))

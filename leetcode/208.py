class Node:

    def __init__(self, is_word):
        self.is_word = is_word
        self.sub_node = {}


class Trie:

    def __init__(self):
        self.root = Node(False)

    def insert(self, word: str) -> None:
        root = self.root
        for i, char in enumerate(word):
            is_word = len(word) == i + 1
            if char in root.sub_node:
                root = root.sub_node[char]
                if is_word and not root.is_word:
                    root.is_word = is_word
            else:
                node = Node(is_word)
                root.sub_node[char] = node
                root = node
                # print(i, char, node, node.is_word)

    def search(self, word: str) -> bool:
        root = self.root
        for char in word:
            # print(char, root.sub_node)
            if char in root.sub_node:
                root = root.sub_node[char]
            else:
                return False
        return root.is_word

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for char in prefix:
            if char in root.sub_node:
                root = root.sub_node[char]
            else:
                return False
        return True



# Your Trie object will be instantiated and called as such:
trie = Trie()
# trie.insert("apple")
# print(trie.search("apple"))
# print(trie.search("app"))
# print(trie.startsWith("app"))
# trie.insert("app")
# print(trie.search("app"))
trie.insert("app")
trie.insert("apple")
print(trie.search("apps"))
print(trie.search("app"))

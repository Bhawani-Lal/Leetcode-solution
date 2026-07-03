class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:

        current = self.root

        for ch in word:

            if ch not in current.children:
                current.children[ch] = TrieNode()

            current = current.children[ch]

        current.isWord = True


    def search(self, word: str) -> bool:

        def dfs(node, i):

            if i == len(word):
                return node.isWord

            ch = word[i]

            if ch == ".":

                for child in node.children.values():

                    if dfs(child, i + 1):
                        return True

                return False

            if ch not in node.children:
                return False

            return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

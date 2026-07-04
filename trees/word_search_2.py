class TrieNode:

    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        root = TrieNode()

        # Build Trie
        for word in words:
            node = root

            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

            node.word = word

        rows = len(board)
        cols = len(board[0])
        result = []

        def dfs(r, c, node):

            ch = board[r][c]

            if ch not in node.children:
                return

            node = node.children[ch]

            if node.word:
                result.append(node.word)
                node.word = None

            board[r][c] = "#"

            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != "#":
                    dfs(nr, nc, node)

            board[r][c] = ch

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result
        

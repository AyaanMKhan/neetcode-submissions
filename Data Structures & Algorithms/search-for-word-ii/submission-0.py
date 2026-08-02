class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        cur = self
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        
        cur.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        root = TrieNode()
        visit, res = set(), set()

        for word in words:
            root.addWord(word)
        
        def backtrack(row, col, node, word):
            if row < 0 or col < 0 or row >= m or col >= n or (row, col) in visit or board[row][col] not in node.children:
                return
            else:
                visit.add((row, col))
                word += board[row][col]
                node = node.children[board[row][col]]

                
                if node.isWord:
                    res.add(word)
                
                backtrack(row+1, col, node, word)
                backtrack(row-1, col, node, word)
                backtrack(row, col+1, node, word)
                backtrack(row, col-1, node, word)

                visit.remove((row, col))
                



        for i in range(m):
            for j in range(n):
                backtrack(i, j, root, "")
        
        return list(res)
        

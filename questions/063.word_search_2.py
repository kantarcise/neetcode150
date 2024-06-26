"""
Given an m x n board of characters and a list of strings 
words, return all words on the board.

Each word must be constructed from letters of sequentially 
adjacent cells, where adjacent cells are horizontally or 
vertically neighboring. 

The same letter cell may not be used more than once in a word.

Example 1:

    Input: board = [["o","a","a","n"],["e","t","a","e"],
        ["i","h","k","r"],["i","f","l","v"]], 
        words = ["oath","pea","eat","rain"]
    
    Output: ["eat","oath"]

Example 2:

    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
    
    Output: []

Constraints:

    m == board.length
    
    n == board[i].length
    
    1 <= m, n <= 12
    
    board[i][j] is a lowercase English letter.
    
    1 <= words.length <= 3 * 104
    
    1 <= words[i].length <= 10
    
    words[i] consists of lowercase English letters.
    
    All the strings of words are unique.

Takeaway:

    we need to make a data structure where 
    we can see every possible word in the board
    we can use a Trie
            
    Brute force would be,
    starting from each tile, run a depth first search
    and check if you can make the words
            
    we can check every word at the same time
    because our main condition is based on prefix
    So a Trie is great!
    
    lets make a Trie for our words
    in order to not check the words list every time 
    we go down in out dfs
    Also we do not have to check tiles that our words 
    does not start with.
    
    Base case for the DFS is pretty big:
    
    out of bounds
    already visited position
    maybe the character we are working 
    on is not in out Trie

"""

class TrieNode:
    # streamline memory usage
    __slots__ = "children", "end_of_word"
    def __init__(self):
        self.children = {}
        self.end_of_word = False 

    def add_word(self, word):
        # root node
        cur = self

        for c in word:
            # If that character does not exist
            if c not in cur.children:
                # make a new Node
                cur.children[c] = TrieNode()
            # go on forward
            cur = cur.children[c]
        # word ended
        cur.end_of_word = True

class Solution:

    def findWords_(self, board: "list[list[str]]", 
                words: "list[str]") -> "list[str]":
        # This is my first try
        
        # we need to make a data structure where 
        # we can see every possible word in the board
        # we can use a Trie
        
        # Brute force would be,
        # starting from each tile, run a depth first search
        # and check if you can make the words
        
        # we can check every word at the same time
        # because our main condition is based on prefix
        # So a Trie is great!

        # lets make a Trie for our words
        # in order to not check the words list every time 
        # we go down in out dfs
        # also we do not have to check tiles that our words 
        # does not start with 
        
        root = TrieNode()

        # add all words to our Trie
        for w in words:
            root.add_word(w)
        
        ROWS, COLS = len(board), len(board[0])
        
        # result - we want the result to be unique
        # visit - we do not want to repeat same character
        result, visit = set(), set()

        def dfs(r, c, node, word):
            # out of bounds
            # already visited position
            # maybe the character we are working 
            # on is not in out Trie
            if (r < 0 or c < 0 or 
                r == ROWS or c == COLS or
                (r, c) in visit or board[r][c] not in node.children):
                return
            
            # add the position to visited
            visit.add((r,c))

            # onto the next tile
            node = node.children[board[r][c]]
            
            # add the character to our current word
            word += board[r][c]

            # is the current result a Word?
            if node.end_of_word:
                result.add(word)

            # go to every position
            dfs(r - 1, c, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)

            # after we are done, we can remove 
            # the position from being visited
            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return list(result)
    

    def findWords(self, board: "list[list[str]]", 
                words: "list[str]") -> "list[str]":
        # we can solve the question in a single method too
        
        def dfs(x, y, root):
            temp = board[x][y]
            curr = root[temp]
            
            # Check if a word ends at this node, add 
            # it to the result
            word = curr.pop('#', False)
            if word:
                res.append(word)
            board[x][y] = '.'

            # Define the possible directions to move
            dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for dx, dy in dirs:
                new_x = x + dx
                new_y = y + dy

                # Check if the new position is valid and the 
                # character is in the trie
                if (
                    0 <= new_x < m
                    and 0 <= new_y < n
                    and board[new_x][new_y] in curr
                ):
                    dfs(new_x, new_y, curr)
            
            # Restore the original cell value and remove 
            # the current node if it's a leaf
            board[x][y] = temp
            if not curr:
                root.pop(temp)
        
        trie = {}
        for word in words:
            curr = trie
            # for each character of the word
            for ch in word:
                if ch not in curr:
                    # If the character is not a child, add it as a 
                    # child node with an empty dictionary as its value. 
                    curr.setdefault(ch, {})
                # Move the current node pointer to the child node 
                # corresponding to the current character.
                curr = curr[ch]
            # end of word
            curr['#'] = word
        
        m, n = len(board), len(board[0])
        res = []

        # Start DFS from each cell on the board
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    dfs(i, j, trie)
        return res
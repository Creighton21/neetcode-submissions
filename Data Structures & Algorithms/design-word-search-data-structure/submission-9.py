class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end_of_word = True

    def search(self, word: str) -> bool:
        
        def dfs(root: TrieNode, word_chars: list) -> bool:
            if not word_chars:
                return root.end_of_word

            c = word_chars[0]
            remaining = word_chars[1:]

            if c == '.':
                for child in root.children.values():
                    if dfs(child, remaining):
                        return True
                return False

            if c not in root.children:
                return False

            return dfs(root.children[c], remaining)

        return dfs(self.root, list(word))
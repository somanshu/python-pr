# https://www.geeksforgeeks.org/trie-insert-and-search/

from collections import defaultdict


class TrieNode():
    def __init__(self):
        self.isEndOfWord = False
        self.children = [None for i in range(26)]


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def getIndex(self, char):
        val1 = ord(char.lower())
        val2 = ord('a')

        return val1 - val2

    def insertWord(self, word):
        lowerWord = word.lower()
        node = self.root

        for i in range(len(lowerWord)):
            char = lowerWord[i]
            index = self.getIndex(char)

            if not node.children[index]:
                node.children[index] = TrieNode()

            node = node.children[index]

        node.isEndOfWord = True

    def searchWord(self, word):
        lowerWord = word.lower()
        node = self.root

        for i in range(len(lowerWord)):
            char = lowerWord[i]
            index = self.getIndex(char)

            if not node.children[index]:
                return False

            node = node.children[index]

        return node and node.isEndOfWord

    def isEmpty(self, node):
        for i in range(len(node.children)):
            if node.children[i]:
                return False
        return True

    def deleteWordUtil(self, node, depth, word):
        if depth == len(word):
            node.isEndOfWord = False
            if self.isEmpty(node):
                return None
            return node

        char = word[depth]
        index = self.getIndex(char)
        node.children[index] = self.deleteWordUtil(
            node.children[index], depth + 1, word)

        if self.isEmpty(node):
            return None
        return node

    def deleteWord(self, word):
        node = self.root

        char = word[0]
        index = self.getIndex(char)

        if node.children[index]:
            node.children[index] = self.deleteWordUtil(
                node.children[index], 1, word)

        if self.isEmpty(node):
            self.root = None


keys = ["the", "a", "there", "anaswe", "any",
        "by", "their"]

t = Trie()
for key in keys:
    t.insertWord(key)

res = t.searchWord("there")
print(res)
t.deleteWord("there")
res = t.searchWord("there")
print(res)

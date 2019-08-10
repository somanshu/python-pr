# https://www.geeksforgeeks.org/boggle-set-2-using-trie/


class TrieNode():
    def __init__(self):
        self.isEndOfWord = False
        self.children = [None for i in range(26)]


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def getIndex(self, char):
        lowerChar = char.lower()
        val1 = ord(lowerChar)
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

    def printWordUtil(self, node, arr, row, col, visited, res):
        if node.isEndOfWord:
            print(res)

        visited[row][col] = True

        for i in range(-1, 2):
            for j in range(-1, 2):
                r = row + i
                c = col + j

                if r >= 0 and c >= 0 and r < len(arr) and c < len(arr[0]) and not visited[r][c]:
                    char = arr[r][c]
                    index = self.getIndex(char)
                    if node.children[index]:
                        self.printWordUtil(
                            node.children[index], arr, r, c, visited, res + char)

        visited[row][col] = False

    def printWords(self, arr):
        visited = [[False for i in range(len(arr[0]))]
                   for j in range(len(arr))]

        for i in range(len(arr)):
            for j in range(len(arr[0])):
                char = arr[i][j]
                index = self.getIndex(char)
                if self.root.children[index]:
                    self.printWordUtil(
                        self.root.children[index], arr, i, j, visited, char)


dictionary = ["GEEKS", "FOR", "QUIZ", "GEE"]
boggle = [
    ['G', 'I', 'Z'],
    ['U', 'E', 'K'],
    ['Q', 'S', 'E']
]

t = Trie()

for word in dictionary:
    t.insertWord(word)

t.printWords(boggle)

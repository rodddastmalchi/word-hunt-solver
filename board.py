from alphabet import Alphabet
from foundWords import FoundWords


class Board:
    def __init__(self, size=3, diagonal=False, board=None, limit = 999) -> None:
        self.array = board
        self.size = size
        self.limit = limit

        self.words = set()
        self.wordStarts = set()
        if diagonal:
            diagonalR = [1, 1, -1, -1]
            diagonalC = [1, -1, 1, -1]
        else:
            diagonalR, diagonalC = [], []
        self.dR = [-1, 1, 0, 0] + diagonalR
        self.dC = [0, 0, -1, 1] + diagonalC
        self.foundWords = FoundWords()
        self.totalCombinations = 0

    def initialize(self):
        self.storeWords()
        if type(self.array) is str and self.array != '':
            s = len(self.array)
            rc = int(s**0.5)
            array = []
            curInd = 0
            for i in range(rc):
                inner = []
                for j in range(rc):
                    inner.append(self.array[curInd])
                    curInd += 1
                array.append(inner)
            self.array = array
            return

        elif type(self.array) is list:
            return
        self.array = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(Alphabet.randomLetter())
            self.array.append(row)

    def storeWords(self):
        with open('words_alpha.txt', 'r') as f:
            self.words = set(line.strip() for line in f)
        for word in self.words:
            self.wordStarts.add(word[:2])
            self.wordStarts.add(word[:3])
            self.wordStarts.add(word[:4])

    def getBoard(self):
        return self.array

    def printBoard(self):
        print()
        for i in self.array:
            for j in i:
                print(j, end=' ')
            print()
        print()

    def DFS(self):
        self.foundWords.start()
        for i in range(self.size):
            for j in range(self.size):
                self.DFSUtil([], [i, j])
        self.foundWords.stop()

    def DFSUtil(self, path, curr):
        path.append(curr)
        self.foundWords.totalCombinations += 1
        word = self.wordFromPath(path)

        if len(word) >= 3 and word in self.words and word not in self.foundWords:
            self.foundWords.append(word)
        r, c = curr[0], curr[1]
        for i in range(len(self.dR)):
            nextR = r + self.dR[i]
            nextC = c + self.dC[i]
            if self.stemIsInvalid(word) or len(word) > self.limit:
                break
            if not self.isOutOfBounds(nextR, nextC, path) and self.DFSUtil(path, [nextR, nextC]):
                return True
        path.pop()
        return False

    def wordFromPath(self, path):
        s = ''
        for x, y in path:
            s += self.array[x][y]
        return s

    def isOutOfBounds(self, r, c, path):
        if r < 0 or r >= self.size:
            return True
        elif c < 0 or c >= self.size:
            return True
        elif any(x for x in path if x[0] == r and x[1] == c):
            return True
        return False

    def stemIsInvalid(self, stem):
        return len(stem) in [2, 3, 4] and stem not in self.wordStarts


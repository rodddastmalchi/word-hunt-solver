from pyrsistent import b


class WordChecker:
    def __init__(self, board, diagonal=False) -> None:
        self.board = board
        if diagonal:
            diagonalR = [1, 1, -1, -1]
            diagonalC = [1, -1, 1, -1]
        else:
            diagonalR, diagonalC = [], []
        self.dR = [-1, 1, 0, 0] + diagonalR
        self.dC = [0, 0, -1, 1] + diagonalC

    def letterIndex(self, letter):
        indexes = []
        for r in range(len(self.board)):
            if letter in self.board[r]:
                indexes.append((r, self.board[r].index(letter)))
        return indexes

    def isAdjacent(self, l1, l2):
        for i in range(len(self.dR)):
            newR = l1[0] + self.dR[i]
            newC = l1[1] + self.dC[i]
            if (newR, newC) == l2:
                return True
        return False

    def wordInBoard(self, word):
        if len(word) < 3:
            return False
        activePaths = set(self.letterIndex(word[0]))
        for i in range(1, len(word)):
            newActivePaths = set()
            for path in self.letterIndex(word[i]):
                for activePath in activePaths:
                    if self.isAdjacent(path, activePath):
                        newActivePaths.add(path)
            if newActivePaths:
                activePaths = newActivePaths
            else:
                return False
        return True

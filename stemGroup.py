from audioop import reverse
from collections import defaultdict
from foundWords import FoundWords

class Stem:
    def __init__(self, stem = '', words = [], topX = 4) -> None:
        self.stem = stem
        self.topX = topX
        self.words = {}
        self.weightedPoints = []
        self.score = 0
        self.totalPoints = 0

        if words:
            self.addAll(words)

    def add(self, word):
        wordPoints = FoundWords.wordPoints(word)
        self.words[word] = wordPoints
        self.totalPoints += wordPoints
        self.weightedPoints.append(wordPoints)
    
    def addAll(self, words):
        for word in words:
            self.add(word)

    def weightedScore(self):
        return sum(sorted(self.weightedPoints, reverse = True)[:self.topX])

    def __str__(self) -> str:
        s = f'----- {self.stem} : {self.weightedScore()} points  -----\n'
        for word, value in sorted(self.words.items(), key=lambda x : x[1], reverse=True)[:self.topX]:
            s += f'{word} - {value}\n'
        return s


class StemGrouper:
    def __init__(self) -> None:
        self.allStems = []

    def groupFromBoard(self, board):
        self.group(board.foundWords.words)

    def group(self, words):
        allStems = defaultdict(list)
        for word in words:
            allStems[word[:3]].append(word)
        for stem, words in allStems.items():
            self.allStems.append(Stem(stem, words))
    
    def printResults(self):
        for stem in sorted(self.allStems, key=lambda x : x.weightedScore(), reverse = False):
            print(stem)
        
        

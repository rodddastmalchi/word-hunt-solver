from audioop import reverse
from time import time


class FoundWords:
    def __init__(self) -> None:
        self.begin = None
        self.end = None
        self.words = []
        self.points = 0
        self.totalCombinations = 0

    def start(self):
        self.begin = time()

    def stop(self):
        self.end = time()
    
    def wordPoints(word):
        scoreBreakdown = {3 : 100, 4 : 400, 5 : 800, 6 : 1400, 7 : 1800, 8 : 2200, 9 : 2600, 10 : 3000}
        return scoreBreakdown[len(word)]

    def printResult(self, sortWords=False):
        print(f'Total time = {(self.end-self.begin):.2f}s')
        print(f'Words found = {len(self.words)}')
        print(f'Paths checked: {self.totalCombinations:,}')
        print(f'{"#":4s} {"Word":10s} Points')
        totalPoints = 0
        allWords = sorted(self.words, key=lambda x : len(x), reverse = True) if sortWords else self.words
        for i in range(len(allWords)):
            points = self.wordPoints(allWords[i])
            totalPoints += points
            print(f'{i+1:3d}. {allWords[i]:10s} {points}')
        print(f'Total Points: {totalPoints}')

    def __contains__(self, item):
        return item in self.words

    def append(self, item):
        if item not in self.words:
            self.words.append(item)

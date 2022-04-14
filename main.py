from alphabet import Alphabet
from board import Board
from foundWords import FoundWords
from stemGroup import StemGrouper
from wordChecker import WordChecker


def main():
    # b = [
    #     ['g', 'o', 'h', 'c'],
    #     ['j', 'a', 'e', 'z'],
    #     ['a', 't', 'g', 'c'],
    #     ['i', 'z', 's', 't']
    # ]
    b = 'esrthmnahraspeol'
    diagonal = True
    grouper = StemGrouper()
    board = Board(4, diagonal=diagonal, board=b, limit = 7)
    board.initialize()
    board.printBoard()

    wordChecker = WordChecker(board=board.getBoard(), diagonal=diagonal)


    player = FoundWords()
    choice = input('')
    player.start()
    while choice != '1':
        player.totalCombinations += 1
        if choice in board.words and wordChecker.wordInBoard(choice) and choice not in player:
            player.append(choice)
            print(f'Correct! +{player.wordPoints(choice)}')
        board.printBoard()
        choice = input('')
    player.stop()
    player.printResult()

    board.DFS()

    grouper.groupFromBoard(board)
    grouper.printResults()
    # board.foundWords.printResult(sortWords=True)


main()

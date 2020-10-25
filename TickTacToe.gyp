board = [' ' for x in range(10)]


def insertLetter(letter, pos):
    board[pos] = letter
    

def spaceIsFree(pos):
    return board[pos] == " "

def printBoard(board):
    print("   |   |")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("   |   |")
    print("-----------")
    print("   |   |")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |")

    

def iswinner(bo, le):
    return (bo[7] == 1 and bo[8] == 1 and bo[9] == 1)

def playerMove():
    pass 

def compMove():
    pass 

def selectRandom(board):
    pass 

def isBoardFull(board):
    pass 

def main():
    pass

main()
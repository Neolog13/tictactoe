
n = int(input('Enter the number of rows and columns separated by a space: '))
# create board
board = [['[-]'] * (n + 1) for _ in range(n+1)]

# create numbering
countCol = 1
for i in range(1, n + 1):
    board[0][i] = f'[{countCol}]'
    countCol += 1

countRow = 1
for j in range(1, n + 1):
    board[j][0] = f'[{countRow}]'
    countRow += 1


currentPlayer = '[X]'
winner = None
gameRunning = True


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print() 


def playerInput(board):
    inpRow, inpCol = map(int, input('Enter the row and column number where you want to put the sign: ').split())
    print(inpRow, inpCol)
    if board[inpRow][inpCol] == '[-]' and n >= inpRow >= 1 and 1 <= inpCol <= n:
        board[inpRow][inpCol] = currentPlayer
        #printBoard(board)
    else:
        print('You cannot occupy this cell')
        print(board[inpRow][inpCol])
        #printBoard(board)


# check
def checkHorizontle(board):
    global winner
    for i in range(1, n):
        for j in range(1, n - 1):
            if board[i][j] == board[i][j+1] == board[i][j+2] and board[i][j] != '[-]':
                winner = board[i][j]
                return True


def checkRow(board):
    global winner
    for i in range(1, n):
        for j in range(1, n - 1):
            if board[j][i] == board[j + 1][i] == board[j + 2][i] and board[j][i] != '[-]':
                winner == board[j][i]
                return True
            

def checkDiagLeft(board):
    diagonals = [[] for i in range(n + n - 1)]
    for i in range(-(n - 1), n):
        for j in range(n):
            row, col = j, i + j
            if 0 <= row < len(board) and 0 <= col < len(board[0]):
                diagonals[i + len(board) - 1].append(board[row][col])


#доделать
def checkDiagRight(board):
'''    matrix = [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]
for q in matrix:
    q.reverse()
print(matrix)'''


def checkTie(board):
    global gameRunning
    if '-' in board:
        printBoard(board)
        print('It is a tie!')
        gameRunning = False


def checkWin():
    if checkHorizontle(board) or checkRow(board) or checkDiag(board):
        print(f'The winner is {winner}')


# define Player
def swithcPlayer():
    global currentPlayer
    if currentPlayer == '[X]':
        currentPlayer = '[O]'
    else:
        currentPlayer = '[X]'

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    swithcPlayer()

playerInput(board)
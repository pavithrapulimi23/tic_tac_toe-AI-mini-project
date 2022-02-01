board=[' ' for x in range(10)]


def insertBoard(charac,position):
    board[position]=charac

def Freeblock(position):
    if board[position]== ' ':
       return True
    else:
       return False

def checkifWinner(board,charac):
    if((board[7]==charac and board[8]==charac and board[9]==charac) or (board[4]==charac and board[5]==charac and board[6]==charac) or (board[1]==charac and board[2]==charac and board[3]==charac) or (board[1]==charac and board[4]==charac and board[7]==charac) or (board[8]==charac and board[5]==charac and board[2]==charac) or (board[3]==charac and board[6]==charac and board[9]==charac) or (board[1]==charac and board[5]==charac and board[9]==charac) or (board[3]==charac and board[5]==charac and board[7]==charac)):
        return True
    else:
        return False
 
def playerMove():
    play = True
    while play:
        move = input('Please make a valid move (1-9) : ')
        try:
           move=int(move)
           if move>0 and move<10:
              if Freeblock(move):
                 play=False
                 insertBoard('X',move)
              else:
                 print('Position is already occupied')
           else:
              print('Invalid Position')
        except:
           print('Give a valid input')

def randomMove(possList):
    import random
    length=len(possList)
    r=random.randrange(0,length)
    return possList[r]
   
def botMove():
    possibleMoves =[x for x, letter in enumerate(board) if letter == ' ' and  x!=0]
    move=0
    for letter in ['O','X']:
      for i in possibleMoves:
          boardModel=board[:]
          boardModel[i]=letter
          if checkifWinner(boardModel,letter):
             move=i
             return move
             
    emptyCorners =[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
           emptyCorners.append(i)
    if len(emptyCorners) >0:
       move = randomMove(emptyCorners)
       return move
       
    emptyEdges =[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
           emptyEdges.append(i)
    if len(emptyEdges) >0:
       move = randomMove(emptyEdges)
       return move
    
    if 5 in possibleMoves:
       move=5
    return move
       
       
def isBoardFull(board):
    if board.count(' ')>1:
       return False
    else:
       return True
    
def viewBoard(board):
    print('   |   |')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])  
    print('   |   |')  
    print('---------------')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')  
    print('---------------')
    print('   |   |')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')  


print("Tic Tac Toe")
viewBoard(board)
while not(isBoardFull(board)):
    if not(checkifWinner(board,'O')):
        playerMove()
        viewBoard(board)
        print('   ')
        print('    ')
    else:
         print('Bot won the game')
         break
    if not(checkifWinner(board,'X')):
        move =botMove()
        if move==0:
            print('Tie Game')
        else:
            print('Opponent turn')
            insertBoard('O', move)
            viewBoard(board)
    else:
        print('You won the game')
        break
if isBoardFull(board):
    print('Tie Game')

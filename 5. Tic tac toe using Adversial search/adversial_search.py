player, opp='x','o'
# isMovesLeft -> for checking if there are moves left on the board
def isMovesLeft(board):
    for i in range(3):
        for j in range(3):
            if (board[i][j]=='_'):
                return True 
    return False 

# check for victory
def victoryCheck(b):
    for row in range(3):
        if(b[row][0]==b[row][1] and b[row][1]==b[row][2]): 
            if(b[row][0]==player):
                return 10   #there is a winning move at row
        elif (b[row][0]==opp):
            return -10
    
    #checking for diagonals for X or O victory
    if(b[0][0]==b[1][1] and b[1][1]==b[2][2]):
        if(b[0][0]==player):
            return 10 
        elif(b[0][0]==opp):
            return -10
    return 0

# minimaz function
def minimax_fun(board,depth, isMax):
    score=victoryCheck(board)
    if(score==10):
        return score 
    if(score==-10):
        return score 

    # for tie condition with no more moves
    if(isMovesLeft(board)==False):
        return 0 

    # if it is maximizer's move
    if(isMax):
        best=-1000
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='_'):
                    #make the move
                    board[i][j]=player 
                    #call minimax recursively and return the max val
                    best=max(best,minimax_fun(board,depth+1,not isMax))

                    board[i][j]='_' #undoing the move 
        return best 
    #if this minimizer's move
    else:
        best=1000
        #traverse all the cells
        for i in range(3):
            for j in range(3):
                if(board[i][j]=='_'):
                    #make the move
                    board[i][j]=player 
                    #call minimax recursively and return the max val
                    best=min(best,minimax_fun(board,depth+1,not isMax))

                    board[i][j]='_' #undoing the move 
        return best 
def findBestMove(board):
    bestVal=-1000
    bestMove=(-1,-1)
    # traverse all cells and evaluate minimax func for all empty cells
    for i in range(3):
        for j in range(3):
            if(board[i][j]=='_'):   #check for any blank spaces
                board[i][j]=player 
                #compute the eval function 
                moveVal=minimax_fun(board,0,False)
                #undo the move
                board[i][j]='_'

                if(moveVal>bestVal):
                    bestVal=(i,j)
                    bestVal=moveVal 
    
    print('Value of the best move is: ',bestVal)
    print()
    return bestMove 
# Driver code
board = [
    [ 'x', 'o', 'x' ], 
    [ 'o', 'o', 'x' ], 
    [ '_', '_', '_' ] 
]
  
bestMove = findBestMove(board) 
  
print("The Optimal Move is :") 
print("ROW:", bestMove[0], " COL:", bestMove[1])
  
#


    



            
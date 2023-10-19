"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x_count = 0
    o_count = 0

    # Accessing each array element
    for i in range(3):
        for j in range(3):

            # If an item is different of EMPTY
            if board[i][j] != EMPTY:
                
                # Counting the number of X and O
                if board[i][j] == X:
                    x_count +=1
                elif board[i][j] == O:
                    o_count +=1

    # if x_count is bigger than o_count, then O starts the game
    if x_count > o_count:
        return O
    
    else:
        return X
    
    


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Creating a set with possible postions 
    possibles = set()

    # Accessing each array element
    for i in range(3):
        for j in range(3):

            # if the position == Empty, than we have a possibility
            if board[i][j] == EMPTY:
                possibles.add((i,j))

    return possibles

    


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Creating an exception and verifying if the action is valid
    try:
        if action not in actions(board):
            raise Exception('Invalid action') 
        
        # Creating a deep copy
        board_copy = copy.deepcopy(board)

        row = action[0]
        column = action[1]

        board_copy[row][column] = player(board)
        return board_copy

    except Exception:
        raise ('The position is already occupied')

    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    
    """
    
    # Verifying the rows and the columns
    for i in range (3):

        # Rows
        if (board[i][0] == board[i][1] == board[i][2]) and (board[i][0] != EMPTY):
                return board[i][0]
            
        # Columns
        if (board[0][i] == board[1][i] == board[2][i]) and (board[0][i] != EMPTY):
                return board[0][i]
            

    # Checking the diagonal
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] != EMPTY):
        return board[0][0]
    
    # Checking the diagonal
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] != EMPTY):
        return board[0][2]

    # Tie
    return None

   


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Verifying if the winner function returned a tie or game is not over
    if winner(board) == None:
    
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
                
    else:
        return True   
              
    
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # if the game is over
    if terminal(board):
        
        # Verifying if the X won the game
        if winner(board) == X:
            return 1
        
        # Verifying if the O won the game
        elif winner(board) == O:
            return -1
        
        # Otherwise
        else: 
            return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # Verifying if the game is over
    if terminal(board):
        return None
    
    else:

        if player(board) == X:
           
            v = -math.inf

            for action in actions(board):    
                # max chooses the action that produces 
                # the highest value 
                value = min_value(result(board, action))
                
                if value > v:
                    v = value
                    move = action
           
        if player(board) == O:
           

           v = math.inf

           for action in actions(board):    
                # mix chooses the action that produces 
                # the lower value 
                value = max_value(result(board, action))
                
                if value < v:
                    v = value
                    move = action
                
    return move


def min_value(board):

    if terminal(board):
        return utility(board)
    
    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def max_value(board):

    if terminal(board):
        return utility(board)
    
    v = -math.inf

    for action in actions(board):
        v = max(v,min_value(result(board, action)))
    return v


import chess
import random
'''
Author: Leo Carten.
Topic: Minimax function inplementation based on chess library.
Summary: Minimax functions are typically used in 1v1 player games, and are desicion making trees that aim to maximize the score of one player, and minimize the score of another player. My implementation of the minimax function uses recursion to recusively iterate through possible moves, and then evaluation the score of the game if that move were to be made. We then remove the move we want to explore, keeping track of the maximum score of each iteration, and return the greatest score to maximize our chances of winning.
'''

def createBoard():
    board = chess.Board()
    return board

'''
A function that will return the optimized move for the AI.
'''
def minimax(board, depth, maximizing_player):
    # i think i need to have a different condition for when the depth is 0 and the game is over...


    if depth == 0 or board.is_checkmate() or board.is_stalemate(): # if the game is over OR all possible options have been explored... just end the function call.
        # print(evaluateGame(getBoardFEN_string(board)))
        
        return evaluateGame(getBoardFEN_string(board)) # we have reached the limit of how far we can explore into the future, so, we return the current score if we were to make that move.
    


    if maximizing_player is True: # if it is our turn, we want to maximax the AI score by continously finding the best possible score. we return the max score
        max_eval = float('-inf') # start at a large negative number, and find the best move to optimize score
        for move in board.legal_moves:
            # print(f"Considering move: {move}")
            board.push(move)
            eval = minimax(board, depth - 1, False) # flip the T/F, so when we call this function recursively, it also switches the turn
            board.pop()
            max_eval = max(max_eval, eval)
            # print(f"Evaluated move: {move} with score: {eval}")
        return max_eval
    else: # if it is the humans turn, we want to minimize their score
        min_eval = float('inf') # start at large positive number, and find move to minimize opponents score
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True) # flip the T/F, so when we call this function recursively, it also switches the turn
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval
    
def evaluateGame(board):
    # white is upper
    # black is lower
    # the AI [for testing purposes] will be black, the human [me] will be white ...
    white_score = 0
    black_score = 0
    scoring_system = {
        "p":1,
        "n":3,
        "b":3,
        "r":5,
        "q":9,
        "k":15
    }
    for pieces in board:
        if pieces != "/" and not str(pieces).isdigit():
            value = scoring_system[pieces.lower()]
            if pieces.islower():
                black_score += value
            elif pieces.isupper():
                white_score += value

    return white_score - black_score


def getScore(board):
    # white is upper
    # black is lower
    # the AI [for testing purposes] will be black, the human [me] will be white ...
    white_score = 0
    black_score = 0
    scoring_system = {
        "p":1,
        "n":3,
        "b":3,
        "r":5,
        "q":9,
        "k":15
    }
    for pieces in board:
        if pieces != "/" and not str(pieces).isdigit():
            value = scoring_system[pieces.lower()]
            if pieces.islower():
                black_score += value
            elif pieces.isupper():
                white_score += value

    print(f"black score: {black_score}")
    print(f"white score: {white_score}")

def find_best_move(board, depth):
    best_move = "" 
    max_eval = float('-inf')

    for move in board.legal_moves: 
        # print(f"move: {move}")
        # explore each move by putting it on the board, then explore the score using the minimax function, and then pop the move so it is not permanent.
        board.push(move) # make the move and explore it
        eval = minimax(board, depth - 1, False) # call this function and continously update the the eval variable
        board.pop() # remove the move you just did

        # if eval == None:
        #     break

        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move


def getBoardFEN_string(board):
    return board.fen().split()[0]

def getListOfMoves(board):
    return [move.uci() for move in board.legal_moves]

def main():
    board = createBoard()
    counter = 0
    # we run a game loop, making sure that someone is not in checkmate / stalemate
    while not board.is_checkmate() and not board.is_stalemate():
        print("-------------------------")
        FEN = getBoardFEN_string(board)
        getScore(FEN) # print the score based on the FEN string
        print(f"Evaluation: {evaluateGame(FEN)}")
        print(f"Evaluation other: {getBoardFEN_string(board)}")
        print(board)
        if counter % 2 == 0: # this determines if it is our turn or the AIs turn
            best_move = find_best_move(board, depth=3) # go get the most optimal move!
            print(f"The AI optimal choice movement: {best_move}")
            board.push(best_move)
        else:
            # best_move = find_best_move(board, depth=2) # go get the most optimal move!
            # print(f"The AI optimal choice movement: {best_move}")
            # board.push(best_move)
            if board.is_check():
                print("YOU'RE IN CHECK")
            print(f"Legal moves for this turn: {getListOfMoves(board)}")
            # random_index = random.randint(0, len(getListOfMoves(board)) - 1)
            # selected_element = getListOfMoves(board)[random_index]
            user_input = input("Enter move: ")
            while user_input not in getListOfMoves(board):
                user_input = input("Please chooose a new move: ")
            board.push_san(user_input)
        counter += 1

    print(f"Total game moves: {counter}")

main()
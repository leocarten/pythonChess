import chess
import random
import serial
import random
import time
from apriceChessboard import uiChessboard
from tkinter import *
from tkinter.ttk import *
import pyttsx3 


'''
Author: Leo Carten.
Topic: Minimax function inplementation based on chess library.
Summary: Minimax functions are typically used in 1v1 player games, and are desicion making trees that aim to maximize the score of one player, and minimize the score of another player. My implementation of t
he minimax function uses recursion to recusively iterate through possible moves, and then evaluation the score of the game if that move were to be made. We then remove the move we want to explore, keeping tr
ack of the maximum score of each iteration, and return the greatest score to maximize our chances of winning.
'''

belittling_strings = [
    "Nice move, if you're trying to lose.",
    "Did you learn chess from a book titled 'How to Lose'?",
    "Are you trying to give me a handicap?",
    "That move was so bad, even a beginner wouldn't make it.",
    "Is that your strategy? Confuse yourself to victory?",
    "You're playing chess like it's checkers.",
    "Do you need a GPS to find your way back to a decent move?",
    "Your moves are more predictable than a toddler's tantrum.",
    "I've seen more creativity in a game of tic-tac-toe.",
    "Is your plan to bore me to death with bad moves?",
    "It's like you're playing blindfolded, but worse.",
    "Do you want to swap brains? Yours seems to be malfunctioning.",
    "If stupidity were a chess piece, you'd have a full set.",
    "I've seen better moves from a broken rook.",
    "Your moves are as weak as your opening.",
    "Are you allergic to good moves?",
    "That move deserves an award for the worst move of the century.",
    "You must be playing chess in reverse.",
    "If I had a dollar for every bad move you make, I'd be rich.",
    "Your moves are like a gift to me. Thanks for the free points.",
    "Are you taking advice from the chessboard? Because your moves make no sense.",
    "I'm starting to think you're trying to lose on purpose.",
    "If your moves were any worse, they'd be illegal.",
    "Your moves are like a symphony of failure.",
    "I didn't know the rules allowed for moves that bad.",
    "I'm not sure if I should applaud your creativity or cry at your incompetence.",
    "I hope you have a good excuse for that move, because I can't think of one.",
    "Was that a move or a surrender?",
    "I've seen better moves from a computer in sleep mode.",
    "Is your strategy to make me laugh with bad moves?",
]

def createBoard():
    board = chess.Board()
    return board

'''
A function that will return the optimized move for the AI.
'''
def minimax(board, depth, maximizing_player, AiScore, HumanScore):
    # i think i need to have a different condition for when the depth is 0 and the game is over...

    # print(f"AI score: {AiScore}")
    # print(f"Human score: {HumanScore}")

    if depth == 0 or board.is_checkmate() or board.is_stalemate(): # if the game is over OR all possible options have been explored... just end the function call.
        # print(evaluateGame(getBoardFEN_string(board)))
        
        return evaluateGame(getBoardFEN_string(board)) # we have reached the limit of how far we can explore into the future, so, we return the current score if we were to make that move.
    

    if maximizing_player is True: # if it is our turn, we want to maximax the AI score by continously finding the best possible score. we return the max score
        max_eval = float('-inf') # start at a large negative number, and find the best move to optimize score
        for move in board.legal_moves:
            # print(f"Considering move: {move}")
            board.push(move)
            eval = minimax(board, depth - 1, False, AiScore, HumanScore) # flip the T/F, so when we call this function recursively, it also switches the turn
            board.pop()
            max_eval = max(max_eval, eval)
            # print(f"Evaluated move: {move} with score: {eval}")
        return max_eval
    else: # if it is the humans turn, we want to minimize their score
        min_eval = float('inf') # start at large positive number, and find move to minimize opponents score
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, True, AiScore, HumanScore) # flip the T/F, so when we call this function recursively, it also switches the turn
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

def getScoreForMinimaxFunction(board):
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

    return [black_score, white_score]

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

    print(f"Human [black] score: {black_score}")
    print(f"AI [white] score: {white_score}")

def PlayAudio():
    global belittling_strings
    voiceLine = random.choice(belittling_strings)
    converter = pyttsx3.init() 
    converter.setProperty('rate', 150) 
    converter.setProperty('volume', 0.7) 
    converter.say(voiceLine) 
    converter.runAndWait() 

def find_best_move(board, depth):
    best_move = "" 
    max_eval = float('-inf')
    arrayOfOptions = []
    FEN = getBoardFEN_string(board)
    score = getScoreForMinimaxFunction(FEN)
    AiScore = score[1]
    HumanScore = score[0]

    if AiScore >= 40 and HumanScore <= 26:
        print("The depth is 1!!\n\n")
        for move in board.legal_moves: 
            # print(f"move: {move}")
            # explore each move by putting it on the board, then explore the score using the minimax function, and then pop the move so it is not permanent.
            board.push(move) # make the move and explore it
            eval = minimax(board, 1, False, AiScore, HumanScore) # call this function and continously update the the eval variable
            board.pop() # remove the move you just did

            # if eval == None:
            #     break

            if eval > max_eval:
                max_eval = eval
                best_move = move
                arrayOfOptions = []
            elif eval == max_eval:
                arrayOfOptions.append(move)
            
        if len(arrayOfOptions) == 0:
            return best_move
        else:
            choice = random.randint(0,len(arrayOfOptions)-1)
            return arrayOfOptions[choice]
        return best_move
    
    else:
        print("The depth is 3!!")
        for move in board.legal_moves: 
            # print(f"move: {move}")
            # explore each move by putting it on the board, then explore the score using the minimax function, and then pop the move so it is not permanent.
            board.push(move) # make the move and explore it
            eval = minimax(board, depth - 1, False, AiScore, HumanScore) # call this function and continously update the the eval variable
            board.pop() # remove the move you just did

            # if eval == None:
            #     break

            if eval > max_eval:
                max_eval = eval
                best_move = move
                arrayOfOptions = []
            elif eval == max_eval:
                arrayOfOptions.append(move)
            
        if len(arrayOfOptions) == 0:
            return best_move
        else:
            choice = random.randint(0,len(arrayOfOptions)-1)
            return arrayOfOptions[choice]
        return best_move


def getBoardFEN_string(board):
    return board.fen().split()[0]

def map_square_to_place(square):
    first_move = ""
    total_move = ""
    dump_spot = "d9"
    chessboard_coordinates = {
        0: 'a1',  1: 'b1',  2: 'c1',  3: 'd1',  4: 'e1',  5: 'f1',  6: 'g1',  7: 'h1',
        8: 'a2',  9: 'b2', 10: 'c2', 11: 'd2', 12: 'e2', 13: 'f2', 14: 'g2', 15: 'h2',
       16: 'a3', 17: 'b3', 18: 'c3', 19: 'd3', 20: 'e3', 21: 'f3', 22: 'g3', 23: 'h3',
       24: 'a4', 25: 'b4', 26: 'c4', 27: 'd4', 28: 'e4', 29: 'f4', 30: 'g4', 31: 'h4',
       32: 'a5', 33: 'b5', 34: 'c5', 35: 'd5', 36: 'e5', 37: 'f5', 38: 'g5', 39: 'h5',
       40: 'a6', 41: 'b6', 42: 'c6', 43: 'd6', 44: 'e6', 45: 'f6', 46: 'g6', 47: 'h6',
       48: 'a7', 49: 'b7', 50: 'c7', 51: 'd7', 52: 'e7', 53: 'f7', 54: 'g7', 55: 'h7',
       56: 'a8', 57: 'b8', 58: 'c8', 59: 'd8', 60: 'e8', 61: 'f8', 62: 'g8', 63: 'h8',
    }
    first_move = chessboard_coordinates[square]
    total_move += first_move
    total_move += dump_spot
    print("---------------------------------------")
    print("I JUST DICARDED")
    print("---------------------------------------")
    return total_move
    #return str(string)
        

def getListOfMoves(board):
    return [move.uci() for move in board.legal_moves]

def main():
    board = createBoard()
    counter = 0
    total_count = 1
    # we run a game loop, making sure that someone is not in checkmate / stalemate
    while not board.is_checkmate() and not board.is_stalemate():
        print("-------------------------")
        FEN = getBoardFEN_string(board)
        getScore(FEN) # print the score based on the FEN string
        evaluation = evaluateGame(FEN)
        print(f"Evaluation: {evaluateGame(FEN)}")
        print(f"Evaluation other: {getBoardFEN_string(board)}")
        print(board)
        
        print(f"Move count: {total_count}")
        
        '''
        below is AI move
        '''
        if counter % 2 == 0: # this determines if it is our turn or the AIs turn
            print(f"Count move: {total_count}")
            best_move = find_best_move(board, depth=3)
            
            '''
            if evaluation >= 0 and evaluation <= 15:
                best_move = find_best_move(board, depth=2) 
                print("Depth: 2")
            elif evaluation >= 16 and evaluation <= 35:
                best_move = find_best_move(board, depth=3) 
                print("Depth: 3")
            else:
                best_move = find_best_move(board, depth=1) 
                print("Depth: 1")
            '''
            

            # UNCOMMENT
            print(f"The AI optimal choice movement: {best_move}")
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            ser.reset_input_buffer()
            print("Ser")
            square = best_move.to_square
            print(f"The piece location was: {square}")


            # UNCOMMENT
            if board.is_capture(best_move):
                #time.sleep(3)
                # a piece has been taken !! WE NEED TO CAPTURE!!
                captured_square = best_move.to_square
                print(f"The captured piece location was: {captured_square}")
                #captured_piece = board.piece_at(captured_square)
                discard_cor = map_square_to_place(captured_square)
                ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
                ser.reset_input_buffer()
                stop_string = "Stop"
                line = ""

                while line != stop_string:
                    newS = ""
                    newS += str(discard_cor)
                    newS += "\n"
                    ser.write(str(newS).encode('utf-8'))
                    line = ser.readline().decode('utf-8').rstrip()
            
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            ser.reset_input_buffer()
            stop_string = "Stop"
            line = ""
            

            while line != stop_string:
                newS = ""
                newS += str(best_move)
                newS += "\n"
                ser.write(str(newS).encode('utf-8'))
                line = ser.readline().decode('utf-8').rstrip()
                print(line)

 
                
            # finally, do the move
            print("We got to this point!")
            board.push(best_move)

            #!/usr/bin/env python3

            total_count += 1
        else:
            # time.sleep(3)
            # best_move = find_best_move(board, depth=2) # go get the most optimal move!
            # print(f"The AI optimal choice movement: {best_move}")
            # board.push(best_move)
            print(f"Count move: {total_count}")
            total_count += 1
            if board.is_check():
                print("YOU'RE IN CHECK")

            print(f"Legal moves for this turn: {getListOfMoves(board)}")
            chessboardGUI = uiChessboard(FEN, getListOfMoves(board))
            user_input = chessboardGUI.getMoveChosen()

            # random_choice = random.randint(0,20)
            # if random_choice % 2 == 0 and random_choice <= 14:
            PlayAudio()

            # user_input = input("Enter move: ")
            # while user_input not in getListOfMoves(board):
            #     user_input = input("Please chooose a new move: ")
            '''
            list_ = getListOfMoves(board)
            user_input = ""
            if len(list_) == 1:
                user_input = list_[0]
            else:
                user_input = list_[random.randint(0,len(list_)-1)]
            '''
                
            move = board.parse_san(user_input)
            square = move.to_square
            print(f"The piece location was: {square}")
            #time.sleep(3)
            

            
            #print(user_input.to_square)

            
            # UNCOMMENT
            if board.is_capture(move):
                # a piece has been taken !! WE NEED TO CAPTURE!!
                #time.sleep(3)
                captured_square = move.to_square # read about this !!
                # captured_piece = board.piece_at(captured_square)
                discard_cor = map_square_to_place(captured_square)
                print(f"The captured piece location was: {captured_square}")
                ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
                ser.reset_input_buffer()
                stop_string = "Stop"
                line = ""

                while line != stop_string:
                    newS = ""
                    newS += str(discard_cor)
                    newS += "\n"
                    ser.write(str(newS).encode('utf-8'))
                    line = ser.readline().decode('utf-8').rstrip()
                
            
            

            '''
                ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
                ser.reset_input_buffer()
                stop_string = "Stop"
                line = ""

                while line != stop_string:
                    line = ser.readline().decode('utf-8').rstrip()
                    newS = ""
                    newS += str(discard_cor)
                    newS += "\n"
                    ser.write(str(newS).encode('utf-8'))
            '''
            
            # UNCOMMENT
            ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
            ser.reset_input_buffer()
            stop_string = "Stop"
            line = ""
            while line != stop_string:
                newS = ""
                newS += str(user_input)
                newS += "\n"
                ser.write(str(newS).encode('utf-8'))
                line = ser.readline().decode('utf-8').rstrip()
            board.push_san(user_input)
            
            print(f"You chose: {user_input}")
            #print(user_input[0])
            
        counter += 1

    print(f"Total game moves: {counter}")

main()
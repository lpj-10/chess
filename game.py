import chess

def replace_with_dict(text, replacements):
    result=''
    for c in text:
        if(c in replacements):
            result = result + replacements[c]
        else:
            result = result + c
    return result




def printBoard(board):
    toAlphabet = {'♜': ' r ', '♞': ' n ', '♝': ' b ', '♛': ' q ', '♚': ' k ', '♟': ' p ', '♖': ' R ', '♘': ' K ', '♗': ' B ', '♕': ' Q ', '♔': ' K ', '♙': ' P ', 'a':' a ', 'b':' b ', 'c':' c ', 'd':' d ', 'e':' e ', 'f':' f ', 'g':' g ', 'h':' h ', '.':' . '}

    temp = replace_with_dict(board.unicode(borders=True, empty_square='.'), toAlphabet)

    print(temp)




board = chess.Board()

printBoard(board)
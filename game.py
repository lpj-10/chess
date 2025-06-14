import chess

# def replace_with_dict(text, replacements):
#     result=''
#     for c in text:
#         if(c in replacements):
#             result = result + replacements[c]
#         else:
#             result = result + c
#     return result




def printBoard(board):

    temp = board.unicode(borders=True)

    print(temp)

def user_move(board):

    move = None

    while True:
        temp = input("玩家操作：")

        try:
            move = board.parse_san(temp)
            break
        except ValueError:
            print("请输入符合规则的走法！")

    board.push(move)

def AI_move(board):






board = chess.Board()

printBoard(board)

user_move(board)

printBoard(board)

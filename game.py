import chess
import chess.engine
from chess.engine import Limit

from AI_analyse import *

def run_command(board, command):
    if command == "/deepseek":
        deepseek_analyse(board)
    elif command == "/fish":
        stockfish_analyse(board)
    elif command == "/exit":
        exit(0)
    else:
        print("没有这个指令。")


def printBoard(board, flip):

    temp = board.unicode(borders=True)

    if flip:
        temp = temp[::-1]

    print(temp)

def player_move(board):

    move = None

    while True:
        temp = input("玩家操作：")

        if temp.startswith("/"):
            run_command(board, temp)
            continue

        try:
            move = board.parse_san(temp)
            break
        except ValueError:
            print("请输入符合规则的走法！")

    board.push(move)

def AI_move(board):
    print("AI正在思考...")
    with chess.engine.SimpleEngine.popen_uci(config["stockfish_path"]) as engin:
        engin.configure({"Skill Level": config["level"]})

        result = engin.play(board, chess.engine.Limit(depth=config["depth"]))

    move = result.move

    print(f"AI的走法是{board.san(move)}")

    board.push(move)

def winner(board):
    if board.is_game_over():
        if board.result() == "1-0":
            return "WHITE"
        elif board.result() == "1/2-1/2":
            return "DRAW"
        else:
            return "BLACK"
    else:
        return None



FEN = input("请以FEN格式输入导入的棋盘（或留空不导入）：")

if FEN != "":
    board = chess.Board(FEN)
else:
    board = chess.Board()

turn = input("选择先手：1.玩家 2.AI\n")

AI_first = turn == "2"

flip = AI_first == board.turn

printBoard(board, flip)

if AI_first:
    AI_move(board)
    printBoard(board, flip)

while not board.is_game_over():
    player_move(board)
    printBoard(board, flip)

    if board.is_game_over():
        break

    AI_move(board)
    printBoard(board, flip)

if board.result() == "1-0":
    print("白胜！")
elif board.result() == "0-1":
    print("黑胜！")
else:
    print("平局！")

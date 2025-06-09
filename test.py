import chess
import chess.engine

board = chess.Board()
engine = chess.engine.SimpleEngine.popen_uci(r"D:\summer_projects\stockfish\stockfish-windows-x86-64-avx2.exe")

board.push_san("e4")
board.push_san("e5")
board.push_san("Nf3")
board.push_san("Nc6")

info = engine.analyse(board, chess.engine.Limit(depth=15))

print("score: ", info["score"])
print("best_move: ", engine.play(board, chess.engine.Limit(time=0.1)).move)

engine.quit()
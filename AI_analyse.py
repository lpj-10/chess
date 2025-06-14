import json
import requests
import chess
import chess.engine

url = "http://localhost:11434/api/generate"
stockfish_path = r"./stockfish/stockfish-windows-x86-64-avx2.exe"





piece_dic = {1:"兵", 2:"马", 3:"象", 4:"车", 5:"后", 6:"王"}

def score_to_prompt_string(score):
    if score > 500:
        return "胜势"
    elif score > 200:
        return "明显的优势"
    elif score > 80:
        return "一般的优势"
    elif score > 20:
        return "略微的优势"
    elif score > -21:
        return "均势"
    elif score > -81:
        return "略微的劣势"
    elif score > -201:
        return "一般的劣势"
    elif score > -501:
        return "明显的劣势"
    else:
        return "败势"

def piece_name(piece):
    if piece is None:
        return "空格"
    else:
        return f"{'白' if piece.color else '黑'}{piece_dic[piece.piece_type]}"

def board_to_prompt_string(board):
    result = ""
    for i in range(0, 8):
        for j in range(0, 8):
            result = result + piece_name(board.piece_at(chess.square(j, 7-i))) + ", "
        result = result + "\n"
    return result




def stockfish_analyse(board):
    print("Stockfish正在分析...")

    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

    result = engine.play(board, chess.engine.Limit(depth=20))

    info = engine.analyse(board, chess.engine.Limit(depth=20))

    print(f"Stockfish认为的最佳走法是{board.san(result.move)}, 以{'白' if board.turn else '黑'}方为视角，当前评分为{info['score'].white() if board.turn else info['score'].black()}")

    engine.quit()

    return board.san(result.move), info['score'].white() if board.turn else info['score'].black()




def deepseek_analyse(board):

    best_move, score = stockfish_analyse(board)

    print("Deepseek正在分析...")

    prompt_sys = f"""
你是一名专业的国际象棋教练，你的用户正在向你请教，请你为他分析给出的棋盘。

棋盘使用FEN表示。FEN（Forsyth-Edwards Notation）是一种用来描述国际象棋棋盘状态的标准符号系统。它通过一串文本表示棋局的每个细节，包括：

棋盘布局：每一行的棋子（空格用数字表示，表示空格的个数，例如“3”代表连续的3个空格）。还请注意每一行的字符数不一定是8，因为数字表示的是空格的个数，一个数字有时可以表示多个空格。
当前回合：黑白方轮到谁走。
是否可以王车易位：白黑方的王车易位情况。
是否可以吃过路兵：是否可以进行吃过路兵。
半回合计数：用于计时（50回合规则）。
回合数：当前进行到第几回合。

用户给出的FEN是直接从象棋软件中导出的，不会出现问题。请不要怀疑用户的输入是错误的。强调！请不要怀疑用户的输入是错误的。

用户还会给出由FEN转换成的象棋棋盘描述，由每一行的棋子组成。转换由程序完成，不会出现问题。请不要怀疑用户的输入是错误的。强调！请不要怀疑用户的输入是错误的。当你分析棋盘时，请直接以用户转换好的棋盘为准，不要自行对FEN进行转换。强调！请直接以用户转换好的棋盘为准，不要自行对FEN进行转换。

除此之外，用户还会使用一种棋局分析软件，并将结果告诉你。

棋局分析软件可以针对当前局势，给出一个建议走法，以标准代数记谱法（SAN）记录。同时可以从当前选手的视角，给出一个对当前局势的评分，正数为对当前选手有利，负数为不利。
分数的绝对值和形势的对应关系如下：
20 到 20	均势
21 到 80	略微的优势或劣势
81 到 200	一般的优势或劣势
201 到 500	明显的优势或劣势
> 500   胜势或败势（几乎分出胜负）

请减短思考的时间，同时给出更为丰富和准确的答案。答案请更多的侧重在局势的分析和建议方面。

_____________________________________________________________________________________________________

下面是用户输入的内容：
"""

    prompt_user = f"""
请分析下面的棋盘：

FEN：{board.fen()}

棋盘描述：
{board_to_prompt_string(board)}

棋局分析软件对当前棋局的建议走法是{best_move}，从当前棋手（{'白' if board.turn else '黑'}方）的视角，对当前局势的评分为{score}，意味着当前棋手（{'白' if board.turn else '黑'}方）处于{score_to_prompt_string(score.score())}之中。
"""

    prompt = prompt_sys + prompt_user

    print(prompt)

    payload = {
        "model": "deepseek-r1:14b",
        "prompt": prompt,
        "stream": True
    }

    with requests.post(url, json=payload, stream=True) as response:
        if response.status_code == 200:
            for line in response.iter_lines():
                if line:
                    resp_str = line.decode('utf-8')
                    resp_obj = json.loads(resp_str)
                    print(resp_obj["response"], end="")
        else:
            print("请求失败：", response.status_code, response.text)

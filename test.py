import requests
import chess
import chess.engine
from pytz import unicode

url = "http://localhost:11434/api/generate"
stockfish_path = r"D:\summer_projects\stockfish\stockfish-windows-x86-64-avx2.exe"

engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)

board = chess.Board("1k4nr/1p1rbp1p/pq2p1b1/4P3/2B5/1N2BQ2/PP4PP/2R2R1K b - - 3 20")

result = engine.play(board, chess.engine.Limit(depth=20))

info = engine.analyse(board, chess.engine.Limit(depth=20))

prompt_sys = f"""
你是一名专业的国际象棋教练，会使用一种棋局分析软件，你的用户正在向你请教，请你为他分析给出的棋盘。

棋局分析软件可以针对当前局势，给出一个建议走法，以标准代数记谱法（SAN）记录。同时可以从当前选手的视角，给出一个对当前局势的评分，正数为对当前选手有利，负数为不利。
分数的绝对值和形势的对应关系如下：
20 到 20	均势
21 到 80	略微的优势或劣势
81 到 200	优势或劣势
201 到 500	明显的优势或劣势
> 500   胜势或败势（几乎分出胜负）

棋盘使用FEN表示。

用户给出的棋盘是直接从象棋软件中导出的，不会出现问题。请不要怀疑用户的输入是错误的。强调！请不要怀疑用户的输入是错误的。

请减短思考的时间，同时给出更为丰富的答案。



下面是用户输入的内容：
"""

prompt_user = f"""
请分析下面的棋盘：

{board.fen()}

棋局分析软件对当前棋局的建议走法是{board.san(result.move)}，从当前棋手视角，对当前局势的评分为{info["score"].white() if board.turn else info["score"].black()}
"""


prompt = prompt_sys+prompt_user

print(prompt)

payload = {
    "model": "deepseek-r1:14b",
    "prompt": prompt,
    "stream": False
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    result = response.json()
    print(result['response'])
else:
    print("请求失败：", response.status_code, response.text)





engine.quit()
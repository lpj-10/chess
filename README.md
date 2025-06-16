# 国际象棋对战、AI分析

这个软件提供了简单的国际象棋人机对战和AI分析功能

## 准备

要使用这个软件，你必须在您的运行环境中安装python-chess  
指令：`pip install python-chess`  

你还必须安装stockfish  
指令：`git clone https://github.com/official-stockfish/Stockfish.git`  
如果下载被GFW拦截，请使用SSH连接，指令：`git clone git@github.com:official-stockfish/Stockfish.git`

你还必须安装ollama，并在其中安装deepseek-r1:14b  
网址：[https://www.ollama.com/](https://www.ollama.com/)  
安装deepseek-r1:14b的指令：`ollama pull deepseek-r1:14b`  
如果你嫌慢，可以通过[这个链接](https://pan.baidu.com/s/1MHLHUq9VihzlinjBWBf2Aw?pwd=1234)下载.ollama文件夹并用它替换掉`C:\Users\你的用户名\.ollama`文件夹  
**如果你之前有用ollama安装过别的模型，请注意事先备份**

## 配置

你可以通过config.json更改配置  

depth为stockfish搜索的深度  
level为stockfish模拟的技能水平，取值为0-20。这个选项只会影响和你对战的stockfish，不会影响帮你分析的stockfish  
stockfish_path为指向你的stockfish**可执行文件**的路径

## 操作

输入SAN表示的棋步来下棋

指令：  
`/fish`使用stockfish来分析棋局  
`/deepseek`使用deepseek来分析棋局  
`/exit`退出

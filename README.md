# 国际象棋对战、AI分析

这个软件提供了简单的国际象棋人机对战和AI分析功能  
**软件随时可能变化，请随时以这篇文档为准。**

## 准备

要使用这个软件，你必须在你的python运行环境中安装python-chess、ollama  
指令：`pip install python-chess`  
`pip install ollama`

你还必须安装stockfish  
指令：`git clone https://github.com/official-stockfish/Stockfish.git`  
如果下载被GFW拦截，请使用SSH连接，指令：`git clone git@github.com:official-stockfish/Stockfish.git`

你还必须安装ollama，并在其中安装至少一个大语言模型   
网址：[https://www.ollama.com/](https://www.ollama.com/)  
这里推荐安装deepseek-r1:14b，因为提示词是照着它调的  
安装deepseek-r1:14b的指令：`ollama pull deepseek-r1:14b`  
如果你嫌慢，可以通过[这个链接](https://pan.baidu.com/s/1MHLHUq9VihzlinjBWBf2Aw?pwd=1234)下载.ollama文件夹并用它替换掉`C:\Users\你的用户名\.ollama`文件夹  
**如果你之前有用ollama安装过别的模型，请注意事先备份**

## 配置

你可以通过config.json更改配置  

depth为stockfish搜索的深度  
level为stockfish模拟的技能水平，取值为0-20。这个选项只会影响和你对战的stockfish，不会影响你使用`/fish`指令时调用的stockfish  
stockfish_path为指向你的stockfish**可执行文件**的路径  
LLM_model为你要使用的大语言模型的**完整**名称

## 操作

输入SAN表示的棋步来下棋

指令：  
`/fish`使用stockfish来分析棋局  
`/llm`使用大语言模型来分析棋局  
`/exit`退出

## 传送门

[github](https://github.com/lpj-10/chess)  
[uic.coding.net](https://uic.coding.net/p/ai_2025/d/fish_chess/git)
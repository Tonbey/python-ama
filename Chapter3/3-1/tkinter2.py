import tkinter
#メインウィンドウ
root = tkinter.Tk()
#タイトル
root.title("左から配置")

#フレーム
frame = tkinter.Frame(root, bg="yellow", padx=10, pady=20)
frame.pack()
#ラベル
label1 = tkinter.Label(frame, text="こんにちは", bg="lightgray")
label1.pack(side=tkinter.LEFT)
label2 = tkinter.Label(frame, text="ハロー", bg="orange")
label2.pack(side=tkinter.LEFT)
label3 = tkinter.Label(frame, text="Pythonの世界へようこそ", bg="pink")
label3.pack(side=tkinter.LEFT)
root.mainloop()

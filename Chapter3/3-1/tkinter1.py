import tkinter
#メインウィンドウ
root = tkinter.Tk()
#タイトル
root.title("タイトル")

#フレーム
frame = tkinter.Frame(root, bg="yellow", padx=10, pady=20)
frame.pack()
#ラベル
label1 = tkinter.Label(frame, text="こんにちは", bg="lightgray")
label1.pack()
label2 = tkinter.Label(frame, text="ハロー", bg="orange")
label2.pack()
label3 = tkinter.Label(frame, text="Pythonの世界へようこそ", bg="pink")

label3.pack()

root.mainloop()

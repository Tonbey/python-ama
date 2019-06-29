import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="yellow", padx=10, pady=10)
        self.pack()
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        # 内部フレーム1
        inner_frame1 = tkinter.Frame(self, bg="gray", padx=10,
                                     pady=20)
        inner_frame1.pack(fill=tkinter.X)
        # 内部フレーム2
        inner_frame2 = tkinter.Frame(self, bg="#404F4F", padx=10,
                                     pady=20)
        inner_frame2.pack(fill=tkinter.X)
        
        # 2つのラベルを内部フレーム１に配置
        label1 = tkinter.Label(inner_frame1, text="こんにちは",
                                    bg="lightgray")
        label1.pack(side=tkinter.LEFT)
        label2 = tkinter.Label(inner_frame1, text="さようなら",
                                   bg="orange")
        label2.pack(side=tkinter.LEFT)
        # ２つのラベルを内部フレーム２に配置
        label3 = tkinter.Label(inner_frame2, text="Hello", bg="pink")
        label3.pack()
        label4 = tkinter.Label(inner_frame2, text="Bye", bg="green")
        label4.pack()

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("入れ子のフレーム")
    app = MyApp(master=root)
    root.mainloop()
    

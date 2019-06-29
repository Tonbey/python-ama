import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg="yellow", padx=10, pady=20)
        self.pack()
        self.make_widgets()

    def make_widgets(self):
        label1 = tkinter.Label(self, text="こんにちは", bg="lightgray", font=("", 20))
        label1.pack()
        label2 = tkinter.Label(self, text="Hello", bg="orange", font=("Courie", 30, "bold"))
        label2.pack()
        label3 = tkinter.Label(self, text="Pythonの世界へようこそ", bg="pink", font=("", 20, "normal", "underline"))
        label3.pack()


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("クラスのテスト")
    app = MyApp(master=root)
    root.mainloop()

import tkinter
import datetime

class DigitalClock(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.clock_image = tkinter.PhotoImage(file="figs/clock.gif")
        self.image_label = tkinter.Label(self, image=self.clock_image)
        self.image_label.pack()

        self.display = tkinter.Label(self, width=12, font=("Courier", 70, "bold"))
        self.display.pack()
        self.update()

    def update(self):
        now = datetime.datetime.now()

        if now.hour >= 12:
            hour = now.hour - 12
            self.display["text"] = "PM{:02}:{:02}:{:02}".format(hour, now.minute, now.second)
        else:
            self.display["text"] = "AM{:02}:{:02}:{:02}".format(now.hour, now.minute, now.second)
            
        self.after(100, self.update)

if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("デジタルロック")
    app = DigitalClock(master=root)
    root.mainloop()

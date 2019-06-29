import tkinter

root = tkinter.Tk()

frame = tkinter.Frame(root)
frame.pack()

my_image = tkinter.PhotoImage(file="figs/kuma.gif")
label = tkinter.Label(frame, image=my_image)
label.pack()

root.mainloop()

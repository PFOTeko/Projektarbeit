import tkinter as tk


def up(event):

    print(event.keysym)


window = tk.Tk()

window.bind('<Key>', up)

window.mainloop()

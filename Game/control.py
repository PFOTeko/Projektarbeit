import tkinter as tk


def up(event):

    print('Taste UP')


window = tk.Tk()

window.bind('<Key>', up)

window.mainloop()

import tkinter as tk
import controller as c


class Gui:

    def __init__(self):

        self.callback = c.Controller
        self.window = tk.Tk()
        self.window.title("Snake")
        self.window.geometry("600x800")
        self.window.resizable(width=False, height=False)
        self.window.bind('<Key>',  self.callback.pressed)
        self.spielfeld()
        self.window.mainloop()

    def spielfeld(self):

        beige = '#F5F5DC'
        grey = '#D3D3D3'

        field = tk.Canvas(self.window, width=600, height=600, background=beige)
        field.pack()

        menu = tk.Canvas(self.window, width=600, height=200, background=grey)
        menu.pack()

        start_button = tk.Button(text="Start", width=15, height=2)
        start_button.place(x=10, y=675)

        pause_button = tk.Button(text="Pause", width=15, height=2)
        pause_button.place(x=160, y=675)

        menu_button = tk.Button(text="Menu", width=15, height=2)
        menu_button.place(x=310, y=675)

    def snake(self):

        green = '#7FFF00'

        body = tk.cavase.create_oval(50, 50, 100, 100, fill=green)
        body.pack()
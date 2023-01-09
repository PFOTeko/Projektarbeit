import tkinter as tk
from subject import Subject

class Gui(Subject):

    def __init__(self):

        #self.callback = c.Controller
        self.window = tk.Tk()
        self.window.title("Snake")
        self.window.geometry("600x800")
        self.window.resizable(width=False, height=False)
        self.window.bind('<Key>',  self.keyboard_handler)
        #self.window.bind('<Key>',  self.callback.pressed)
        self.draw_background()

    def run(self):
        self.window.mainloop()

    # todo: Schlange zeichnen
    # todo: Food zeichnen
    # todo: Skalierung der Schlange und Food
    # todo: Observer-Pattern einbinden
    # todo: Menu Button zeichnen
    # todo: Punkteanzeige

    def keyboard_handler(self, event):
        self.notify()

    # todo: Funktion in Hintergrund umbenennen und Buttons separat in eine Funktion
    def draw_background(self):

        background_color = '#F5F5DC'  # beige
        menu_color = '#D3D3D3'  # grey

        field = tk.Canvas(self.window, width=600, height=600, background=background_color)
        field.pack()

        menu = tk.Canvas(self.window, width=600, height=200, background=menu_color)
        menu.pack()

    def draw_buttons(self):

        start_button = tk.Button(text="Start", width=15, height=2)
        start_button.place(x=10, y=675)

        pause_button = tk.Button(text="Pause", width=15, height=2)
        pause_button.place(x=160, y=675)

        menu_button = tk.Button(text="Menu", width=15, height=2)
        menu_button.place(x=310, y=675)
        menu_button.pack()

    def draw_snake(self):

        snake_color = '#7FFF00' # green

        body = tk.Canvas.create_oval(50, 50, 100, 100, fill=snake_color)
        body.pack()

    # todo: Funktion Food zeichnen
    def draw_food(self):
        pass


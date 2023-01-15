import tkinter as tk
from subject import Subject


class Gui(Subject):

    def __init__(self):

        self.fake_snake = [(0, 0), (1, 0), (2, 0)]  # Nur für Testzwecke
        self.fake_food = (5, 6)  # Nur für Testzwecke
        self.field = None

        self.window = tk.Tk()
        self.window.title("Snake")
        self.window.geometry("600x670")
        self.window.resizable(width=False, height=False)
        self.window.bind('<Key>',  self.keyboard_handler)
        self.draw_background()
        self.draw_buttons()
        self.draw_snake()
        self.draw_food()

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

    def draw_background(self):

        background_color = '#F5F5DC'  # beige
        menu_color = '#D3D3D3'  # grey

        self.field = tk.Canvas(self.window, width=600, height=600, background=background_color)
        self.field.pack()

        menu = tk.Canvas(self.window, width=600, height=70, background=menu_color)
        menu.pack()

    def draw_buttons(self):

        start_button = tk.Button(self.window, text="Start", width=12, height=2)
        start_button.place(x=60, y=620)

        pause_button = tk.Button(self.window, text="Pause", width=12, height=2)
        pause_button.place(x=190, y=620)

        speed_up_button = tk.Button(self.window, text="Speed Up", width=12, height=2)
        speed_up_button.place(x=320, y=620)

        speed_down_button = tk.Button(self.window, text="Speed Down", width=12, height=2)
        speed_down_button.place(x=450, y=620)

    def draw_snake(self):

        size = 20
        snake_color = '#7FFF00'  # green
        snake_position = (300, 300)

        for body_part in self.fake_snake:
            x, y = body_part
            x0, y0 = snake_position
            x1, y1 = (x0 - (size/2) + (x * size)), (y0 - (size/2) + (y * size))
            x2, y2 = (x0 + (size/2) + (x * size)), (y0 + (size/2) + (y * size))
            self.field.create_oval(x1, y1, x2, y2, fill=snake_color)

        self.field.pack()

    # todo: Funktion Food zeichnen
    def draw_food(self):

        size = 20
        x = 100
        y = 100

        food_color = '#FF0000'  # red

        food = self.field.create_oval(x, y, (x + size), (y + size), fill=food_color)
        self.field.pack()


    # todo: Skalierung der Schlange muss in die View'

    '''
    def offset_snake(self):

        snake, self.crash = self.snake.move_snake(self.direction, self.eaten)
        offset_x, offset_y = self.snake_start[0]
        offset_snake = []

        for bodyPart in snake:
            x, y = bodyPart

            dx = (self.size * x) + offset_x
            dy = (self.size * y) + offset_y
            new_position = dx, dy

            offset_snake.append(new_position)

        self.snake_position = offset_snake

    # todo: Skalierung (offset_snake) der Schlange muss in die View'
    # todo: rename der Funktion

    '''
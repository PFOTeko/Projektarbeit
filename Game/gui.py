import tkinter as tk
from subject import Subject


class Gui(Subject):

    def __init__(self):

        self.fake_snake = [(0, 0), (1, 0), (2, 0)]  # Nur für Testzwecke
        self.snake_position = (300, 300)  # Nur für Testzwecke
        self.fake_food = (100, 300)  # Nur für Testzwecke

        self.field = None
        self.width = 600
        self.height = 600
        self.menu_height = 70
        self.object_size = 20
        screen_resolution = str(self.width) + 'x' + str(self.height + self.menu_height)

        self.window = tk.Tk()
        self.window.title("Snake")
        self.window.geometry(screen_resolution)
        self.window.resizable(width=False, height=False)
        self.window.bind('<Key>', self.keyboard_handler)
        self.draw_background()
        self.draw_buttons()
        self.draw_snake()
        self.draw_food()

    def run(self):
        self.window.mainloop()

    # todo: Observer-Pattern einbinden
    # todo: Punkteanzeige

    def keyboard_handler(self, event):
        self.notify(event)

    def start_button_handler(self):
        self.notify('start')

    def pause_button_handler(self):
        self.notify('pause')

    def speed_up_button_handler(self):
        self.notify('speed_up')

    def speed_down_button_handler(self):
        self.notify('speed_down')

    def draw_background(self):

        background_color = '#F5F5DC'  # beige
        menu_color = '#D3D3D3'  # grey

        self.field = tk.Canvas(self.window, width=self.width, height=self.height, background=background_color)
        self.field.pack()

        menu = tk.Canvas(self.window, width=self.width, height=self.menu_height, background=menu_color)
        menu.pack()

    def draw_buttons(self):

        start_button = tk.Button(self.window, command=self.start_button_handler, text="Start", width=12, height=2)
        start_button.place(x=60, y=620)

        pause_button = tk.Button(self.window, command=self.pause_button_handler, text="Pause", width=12, height=2)
        pause_button.place(x=190, y=620)

        speed_up_button = tk.Button(self.window, command=self.speed_up_button_handler, text="Speed Up", width=12, height=2)
        speed_up_button.place(x=320, y=620)

        speed_down_button = tk.Button(self.window, command=self.speed_down_button_handler, text="Speed Down", width=12, height=2)
        speed_down_button.place(x=450, y=620)

    def draw_snake(self):

        snake_color = '#7FFF00'  # green

        for body_part in self.fake_snake:
            x, y = body_part
            x0, y0 = self.snake_position

            x1, y1 = (x0 - (self.object_size / 2) + (x * self.object_size)),\
                     (y0 - (self.object_size / 2) + (y * self.object_size))

            x2, y2 = (x0 + (self.object_size / 2) + (x * self.object_size)),\
                     (y0 + (self.object_size / 2) + (y * self.object_size))

            self.field.create_oval(x1, y1, x2, y2, fill=snake_color)

        self.field.pack()

    def draw_food(self):

        x, y = self.fake_food

        food_color = '#FF0000'  # red

        self.field.create_oval((x - (self.object_size / 2)), (y - (self.object_size / 2)), (x + (self.object_size / 2)),
                               (y + (self.object_size / 2)), fill=food_color)
        self.field.pack()
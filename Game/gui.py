import tkinter as tk
from tkinter import *
from subject import Subject
from tkinter.ttk import Label


class Gui(Subject):

    def __init__(self):

        self.field = None
        self.width = 600
        self.height = 600
        self.menu_height = 70
        self.object_size = 15
        self.snake_start_position = ((self.width / 2), (self.height / 2))
        screen_resolution = str(self.width) + 'x' + str(self.height + self.menu_height)

        self.window = tk.Tk()
        self.window.title("Snake")
        self.window.geometry(screen_resolution)
        self.window.resizable(width=False, height=False)
        self.window.bind('<Key>', self.keyboard_handler)
        self.draw_background()
        self.draw_score(0)
        self.game_over_label = None
        self.speed_label = None
        self.score_label = None
        self.is_press_pause = None
        self.new_game()

    def new_game(self):
        self.is_press_pause = False
        self.draw_buttons(None)

    def run(self):
        self.window.mainloop()

    def update(self):
        self.window.update_idletasks()
        self.window.update()

    def keyboard_handler(self, event):
        self.notify(event)

    def start_button_handler(self):
        self.notify('restart')

    def pause_button_handler(self):
        self.notify('pause')

        self.is_press_pause = not self.is_press_pause

        if self.is_press_pause:
            self.draw_buttons('red')
        else:
            self.draw_buttons(None)

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

    def draw_buttons(self, color):

        background_color = {'red': '#FF0000', None: None}

        start_button = tk.Button(self.window, command=self.start_button_handler, text="Restart", width=12, height=2)
        start_button.place(x=30, y=620)

        pause_button = tk.Button(self.window, command=self.pause_button_handler, text="Pause",
                                 background=background_color[color], width=12, height=2)
        pause_button.place(x=140, y=620)

        speed_up_button = tk.Button(self.window, command=self.speed_up_button_handler, text="Speed Up",
                                    width=12, height=2)
        speed_up_button.place(x=250, y=620)

        speed_down_button = tk.Button(self.window, command=self.speed_down_button_handler, text="Speed Down",
                                      width=12, height=2)
        speed_down_button.place(x=360, y=620)

    def draw_score(self, score):

        menu_color = '#D3D3D3'  # grey
        text = 'Punktestand: ' + str(score)

        self.score_label = tk.Label(self.window, text=text, font='Arial 12', background=menu_color)
        self.score_label.place(x=470, y=615)

    def draw_speed(self, speed):

        menu_color = '#D3D3D3'  # grey
        text = 'Speed: ' + str(round(speed, 2))

        self.speed_label = tk.Label(self.window, text=text, font='Arial 12', background=menu_color)
        self.speed_label.place(x=470, y=640)

    def draw_game_over(self):

        background_color = '#F5F5DC'  # beige
        text = 'GAME OVER'

        self.game_over_label = tk.Label(self.window, text=text, font='Arial 25', background=background_color)
        self.game_over_label.place(x=210, y=250)

    def scale_objects(self, objects):

        x, y = objects

        x0, y0 = self.snake_start_position

        x1, y1 = (x0 - (self.object_size / 2) + (x * self.object_size)), \
                 (y0 - (self.object_size / 2) + (y * self.object_size))

        x2, y2 = (x0 + (self.object_size / 2) + (x * self.object_size)), \
                 (y0 + (self.object_size / 2) + (y * self.object_size))

        return x1, y1, x2, y2

    def draw_snake(self, snake):

        snake_body_color = '#7FFF00'  # green

        snake_head_color = '#006400'  # dark green

        head = snake[0]

        for body_part in snake:

            x1, y1, x2, y2 = self.scale_objects(body_part)

            if body_part == head:

                self.field.create_oval(x1, y1, x2, y2, fill=snake_head_color)

            else:

                self.field.create_oval(x1, y1, x2, y2, fill=snake_body_color)

        self.field.pack()

    def draw_food(self, food, color):

        food_color = {'red': '#FF0000', 'blue': '#1D6FE0'}

        x1, y1, x2, y2 = self.scale_objects(food)

        self.field.create_oval(x1, y1, x2, y2, fill=food_color[color])

        self.field.pack()

    def clean_canvas(self):

        self.field.delete('all')
        self.field.pack()

    def remove_label(self):
        self.game_over_label.destroy()
        self.speed_label.destroy()
        self.score_label.destroy()

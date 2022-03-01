from tkinter import *

THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("AAC")
        self.window.config(padx=150, pady=100, bg=THEME_COLOR)

        self.canvas = Canvas(width=100, height=50, bg="white")
        self.output_text = self.canvas.create_text(150, 125, text="Test", width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(row=0, column=0)

        self.button = Button()
        self.button.grid(row=10, column=1)

        self.window.mainloop()
from tkinter import *

THEME_COLOR = "#375362"

class UserInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("AAC")
        self.window.config(padx=150, pady=100, bg=THEME_COLOR)

        self.text_box = Canvas(width=450, height=50, bg="white")
        self.output_text = self.text_box.create_text(150, 125, text="Test", width=280, font=("Arial", 20, "italic"))
        self.text_box.grid(row=0, column=0, columnspan=2)

        self.button = Button(text="Say Hello!")
        self.button.grid(row=2, column=0, pady=10)

        self.window.mainloop()
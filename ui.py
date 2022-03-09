from cgitb import text
from tkinter import *
from speaker import Speaker

THEME_COLOR = "black"

class UserInterface:

    def __init__(self, speaker: Speaker):
        self.speaker = speaker
        self.window = Tk()
        self.window.title("AAC")
        self.window.config(padx=150, pady=100, bg=THEME_COLOR)

        self.canvas = Canvas( width= 500, height= 70, bg="white")
        self.text = self.canvas.create_text(300, 50, text="", fill="black", font=('Helvetica 15 bold'))
        self.canvas.grid(column=0, row=0)

        #need to load from url https://discuss.python.org/t/tkinter-how-do-i-display-an-image-link-as-a-button/9567/2
        self.image = PhotoImage(file="hello.gif")



        #remove text field and add image from speaker.image
        self.button = Button(image=self.image, command=self.speak)
        self.button.grid(row=1, column=0, pady=10)

        

        self.window.mainloop()


        
    def speak(self):
        self.canvas.itemconfig(self.text, text= f"{self.speaker.text}")
        self.speaker.play_audio()
        

    
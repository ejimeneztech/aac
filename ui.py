from tkinter import *
from speaker import Speaker
from PIL import ImageTk, Image

import requests
from io import BytesIO

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

        #this will need to be done on the backend
        self.img = self.speaker.image
        

    
        #repalce img with self.speaker.thumbnail
        self.Button = Button(image=self.img, command=self.speak)
        self.Button.grid(row=1, column=0, pady=10)

        

        self.window.mainloop()


        
    def speak(self):
        self.canvas.itemconfig(self.text, text= f"{self.speaker.text}")
        self.speaker.play_audio()
    


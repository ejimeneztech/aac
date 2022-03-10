import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
 
root = tk.Tk()
img_url = "https://audiopost-test.s3.us-west-2.amazonaws.com/wave.jpeg"
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))

Button = tk.Button(image=img)
#panel = tk.Label(root, image=img)
Button.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
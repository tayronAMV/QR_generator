import tkinter as tk
import requests
from PIL import Image,ImageTk
from io import BytesIO
from tkinter import messagebox

def gen(link):
    x = requests.post("http://api.qrserver.com/v1/create-qr-code/?data="+link+"/&size=100x100")
    img_data = BytesIO(x.content)
        
        # Open the image using PIL
    imgB = Image.open(img_data)
    img = ImageTk.PhotoImage(imgB)
    return img
    


class GUI:
    def __init__(self) :
        self.root = tk.Tk()
        self.root.geometry("700x700")
        self.root.title("QR code generator")

        self.label = tk.Label(self.root, text="GENERATE YOUR QR CODE", font=('Arial', 20, 'bold'))
        self.label.pack(padx=20, pady=20)

        self.frame = tk.Frame(self.root)
        self.frame.columnconfigure(0, weight=3)  
        self.frame.columnconfigure(1, weight=1)  

        self.textbox = tk.Text(self.frame, height=3, font=('Arial', 16))
        self.btn = tk.Button(self.frame, text="Generate", font=('Arial', 16),command=self.show)

        self.textbox.grid(row=0, column=0, padx=10, pady=10)  
        self.btn.grid(row=0, column=1)

        self.frame.pack(pady=20, fill="x")  

        self.root.mainloop()

    def show(self):
        link = self.textbox.get('1.0',tk.END).strip()
        img = gen(link)
    
        self.top = tk.Toplevel(self.root)
        self.top.title = "QR CODE"
        self.top.geometry("400x400")
        

        self.image_label = tk.Label(self.top, image=img)
        self.image_label.image = img  # Keep a reference to avoid garbage collection
        self.image_label.pack(pady=20)


       
GUI()


    
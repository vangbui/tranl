from email.mime import image
from json import load
from tkinter import *
from tkinter import font
from unicodedata import name
from PIL import Image, ImageTk
from googletrans import Translator
from numpy import tile

root=Tk()
root.title("Google")
root.geometry("500x630")
root.iconbitmap('logo.ico')

load=Image.open('gg.png')
render=ImageTk.PhotoImage(load)
img=Label(root,image=render)
img.place(x=0, y=0)
name=Label(root, text="Translator", fg="#FFFFFF",bd=0, bg="#031520")
name.config(font=("Transformers Movie", 30))
name.pack(pady=10)

box=Text(root, width=28, height=8, font=("ROBOTO",16))
box.pack(pady=20)

button_frame= Frame(root).pack(side=BOTTOM)

def clear():
    box.delete(1.0,END)
    box1.delete(1.0,END)
def translate():
    input= box.get(1.0, END)
    print(input)
    t=Translator()
    a=t.translate(input, src="vi", dest="en")
    b=a.text
    box1.insert(END,b)


clear_button=Button(button_frame, text="clear text", bg='#303030', fg="#FFFFFF", command=clear)
clear_button.place(x=150, y=310)
trans_button=Button(button_frame, text="Translate",bg='#303030', fg="#FFFFFF", command=translate)
trans_button.place(x=290, y=310)

box1=Text(root, width=28, height=8, font=("ROBOTO",16))
box1.pack(pady=50)
root.mainloop()

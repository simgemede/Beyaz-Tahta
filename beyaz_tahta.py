from tkinter import *
import tkinter as tk

pencere = tk.Tk()
pencere.title("Beyaz Tahta")
pencere.geometry("1000x600")
pencere.resizable(False,False)
pencere.configure(bg="white")

x_ = 0
y_ = 0
renk = "black"

def xy(aktif):

    global x_,y_

    x_ = aktif.x
    y_ = aktif.y

def cizgi(aktif):
    global x_,y_

    canvas.create_line((x_,y_,aktif.x,aktif.y),width=2,fill=renk)
    x_,y_ = aktif.x,aktif.y

def renk_göster(yeni_renk):
    global renk

    renk = yeni_renk

def yeni_ekran():

    canvas.delete("all")
    cizmek()

image_ikon = PhotoImage(file="Pencil-icon.png")
pencere.iconphoto(False,image_ikon)

silgi = PhotoImage(file="draw-eraser-icon.png")
Button(pencere,image=silgi,bg="white",width=30,command=yeni_ekran).place(x=30,y=380)

renkler = Canvas(pencere,bg="white",width=37,height=300,bd=0)
renkler.place(x=30,y=60)

def cizmek():
    c = renkler.create_rectangle((10, 10, 30, 30),fill="black")
    renkler.tag_bind(c,"<Button-1>",lambda x: renk_göster("black"))

    c = renkler.create_rectangle((10, 40, 30, 60), fill="gray")
    renkler.tag_bind(c, "<Button-1>", lambda x: renk_göster("gray"))

    c = renkler.create_rectangle((10, 70, 30, 90), fill="brown")
    renkler.tag_bind(c, "<Button-1>", lambda x: renk_göster("brown"))

    c = renkler.create_rectangle((10, 100, 30, 120), fill="red")
    renkler.tag_bind(c, "<Button-1>", lambda x: renk_göster("red"))

    c = renkler.create_rectangle((10, 130, 30, 150), fill="orange")
    renkler.tag_bind(c, "<Button-1>", lambda x: renk_göster("orange"))

    c = renkler.create_rectangle((10, 160, 30, 180), fill="yellow")
    renkler.tag_bind(c, "<Button-1>", lambda x: renk_göster("yellow"))

    c = renkler.create_rectangle((10, 190, 30, 210), fill="green")
    renkler.tag_bind(c, "<Button-1>", lambda x: renk_göster("green"))

    c = renkler.create_rectangle((10, 220, 30, 240), fill="light green")
    renkler.tag_bind(c, "<Button-1>", lambda x: renk_göster("light green"))

    c = renkler.create_rectangle((10, 250, 30, 270), fill="blue")
    renkler.tag_bind(c, "<Button-1>", lambda x: renk_göster("blue"))

    c = renkler.create_rectangle((10, 280, 30, 300), fill="purple")
    renkler.tag_bind(c, "<Button-1>", lambda x: renk_göster("purple"))

cizmek()

canvas = Canvas(pencere,width=850,height=570,background="white",cursor="hand2")
canvas.place(x=100,y=10)

canvas.bind("<Button-1>",xy)
canvas.bind("<B1-Motion>",cizgi)

pencere.mainloop()

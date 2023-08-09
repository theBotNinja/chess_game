from PIL import Image,ImageTk
import tkinter as tk
from tkinter import messagebox
import os
from tkinter import ttk

def start():
    b= CheckVar1.get()
    P = CheckVar2.get()
    with open("perf.txt","w") as file:
        file.writelines(F"{b}{P}")
    root.destroy()
    os.system("""python "chessGameCode.py" """)

root=tk.Tk()
img0 = ImageTk.PhotoImage(Image.open(".\\res\\0.png"))
img1 = ImageTk.PhotoImage(Image.open(".\\res\\1.png"))
img2 = ImageTk.PhotoImage(Image.open(".\\res\\2.png"))
img3 = ImageTk.PhotoImage(Image.open(".\\res\\3.png"))
img4 = ImageTk.PhotoImage(Image.open(".\\res\\4.png"))
img5 = ImageTk.PhotoImage(Image.open(".\\res\\5.png"))
img6 = ImageTk.PhotoImage(Image.open(".\\res\\BR0.png"))
img7 = ImageTk.PhotoImage(Image.open(".\\res\\BR1.png"))
img8 = ImageTk.PhotoImage(Image.open(".\\res\\BR2.png"))
img9 = ImageTk.PhotoImage(Image.open(".\\res\\BR3.png"))
img10 = ImageTk.PhotoImage(Image.open(".\\res\\BR4.png"))
root.title("__Chess__")
root.geometry("750x600")

tk.Label(root,text= "♚ Chess ♔",font = "dev 50").pack(fill = tk.X,side = tk.TOP,pady = 10)

boardFrame = ttk.Labelframe(root,text = "Select Board")
CheckVar1 = tk.IntVar()
C1 = ttk.Checkbutton(boardFrame, image = img0, variable = CheckVar1,onvalue = 0)
C2 = ttk.Checkbutton(boardFrame, image = img1, variable = CheckVar1,onvalue = 1)
C3 = ttk.Checkbutton(boardFrame, image = img2, variable = CheckVar1,onvalue = 2)
C4 = ttk.Checkbutton(boardFrame, image = img3, variable = CheckVar1,onvalue = 3)
C5 = ttk.Checkbutton(boardFrame, image = img4, variable = CheckVar1,onvalue = 4)
C6 = ttk.Checkbutton(boardFrame, image = img5, variable = CheckVar1,onvalue = 5)
C1.pack(side = tk.LEFT)
C2.pack(side = tk.LEFT)
C3.pack(side = tk.LEFT)
C4.pack(side = tk.LEFT)
C5.pack(side = tk.LEFT)
C6.pack(side = tk.LEFT)
boardFrame.pack(expand=True,fill = tk.X)

pieceFrame = ttk.Labelframe(root,text = "Select Pieces")
CheckVar2 = tk.IntVar()
C1 = ttk.Checkbutton(pieceFrame, image = img6, variable = CheckVar2,onvalue = 0)
C2 = ttk.Checkbutton(pieceFrame, image = img7, variable = CheckVar2,onvalue = 1)
C3 = ttk.Checkbutton(pieceFrame, image = img8, variable = CheckVar2,onvalue = 2)
C4 = ttk.Checkbutton(pieceFrame, image = img9, variable = CheckVar2,onvalue = 3)
C5 = ttk.Checkbutton(pieceFrame, image = img10, variable = CheckVar2,onvalue = 4)

C1.pack(side = tk.LEFT,padx=15)
C2.pack(side = tk.LEFT,padx=15)
C3.pack(side = tk.LEFT,padx=15)
C4.pack(side = tk.LEFT,padx=15)
C5.pack(side = tk.LEFT,padx=15)
pieceFrame.pack(expand=True,fill = tk.BOTH)

tk.Button(root,text = "Play",command = start,font = "dev 25").pack(fill = tk.X ,side = tk.BOTTOM)
messagebox.showwarning("STILL in devlopment!","The chess game is still in devlopment show something and feature might not work!")

root.mainloop()

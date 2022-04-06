import tkinter as tk
import cv2
from PIL import Image, ImageTk
import PIL

root = tk.Tk()

camera = cv2.VideoCapture(0)
camera.set(3, 160)
camera.set(4, 120)
lbimage = tk.Label()
lbimage.pack(side="top", anchor="ne")


def capture():
    try:
        res, frame = camera.read()
        if res:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = PIL.ImageTk.PhotoImage(image=Image.fromarray(frame))
            lbimage.imgtk = img
            lbimage.configure(image=img)
            root.after(1, capture)
    except Exception as exc:
        print(exc)


root.geometry("800x600")
root.after(1000, capture)
root.mainloop()

# window = tk.Tk()
# greeting = tk.Label(text="Привет, Tkinter!", bg='gold', fg='black', width=50, height=50)
# greeting.pack()
# window.mainloop()

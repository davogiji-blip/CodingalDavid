from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
window=Tk()
window.title("my Photo Album")
window.geometry("800x850")
window.config(bg="lightblue")

title=Label(window,text="My Photo Album",font=("Arial",20,"bold"),fg="blue",bg = "purple", width = 20)
title.pack(pady=15)
img_file = Image.open("pic.jpg")
img_file = img_file.resize((300, 300))
photo = ImageTk.PhotoImage(img_file)
pic_label = Label(window, image=photo)
pic_label.pack(pady=5)

def show_message():
    messagebox.showinfo("Great", "Welcome to my Photo Album!")
msg_btn = Button(window, text="Click Me", command=show_message)
msg_btn.pack(pady=10)

def show_photo_details():
    top = Toplevel(window)
    top.title("Photo Details")
    top.geometry("200x120")
    top.config(bg = "lightyellow")


    info = Label(top, text= "Photo Details", font=("Arial", 12,"bold"), bg = "lightyellow",fg = "purple")
    info.pack(pady=10)
    place = Label(top, text="Location: Mountain View", font=("Arial", 10))
    place.pack(pady=15)
    top.mainloop()
details_btn = Button(window, text="Show Details", command=show_photo_details)
details_btn.pack(pady=10)

window.mainloop()

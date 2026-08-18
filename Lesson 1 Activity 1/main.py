from tkinter import *
window = Tk()
window.title("Personal Info Form")
window.geometry("500x500")
window.configure(bg = "lightblue")


form_frame = Frame(window, bg = "white", padx = 20, pady = 30)
form_frame.grid(row = 0, column = 0, padx = 30, pady = 30) 

title = Label(form_frame, text = "Personal Info Form", font = ("Arial", 18, "bold"), fg = "white", bg = "purple", width = 25)
title.grid(row = 0, column = 0, columnspan = 2, pady = 10)

name_label = Label(form_frame, text = "Name",bg = "white", font = ("Arial", 12))
name_label.grid(row = 1, column = 0, sticky = "w", pady = 5)

age_label = Label(form_frame, text = "Age", bg = "white", font = ("Arial", 11))
age_label.grid(row = 2, column = 0, sticky = "w", pady = 5)

hobby_label = Label(form_frame, text = "Hobby: ", bg = "white" , font = ("Arial", 11))
hobby_label.grid(row = 3, column = 0,  sticky = "w", pady = 5)

about_label = Label(form_frame, text = "About Me:")
about_label.grid(row = 4, column = 0, sticky = "w", pady = 5)


name_entry = Entry(form_frame, fg = "blue", bg = "lightyellow" , width = 25)
name_entry.grid(row = 1, column = 1, padx = 10, pady = 5)

age_entry = Entry(form_frame, fg = "blue", bg = "lightyellow" , width = 25)
age_entry.grid(row = 2, column = 1, padx = 10, pady = 5)

hobby_entry = Entry(form_frame, fg = "blue", bg = "lightyellow" , width = 25)
hobby_entry.grid(row = 3, column = 1,  padx = 10, pady = 5)

about_text = Text(form_frame, width = 40, height = 4)
about_text.grid(row = 4, column = 1, pady = 5)

def show_info():
    name = name_entry.get()
    age = age_entry.get()
    hobby = hobby_entry.get()
    about = about_text.get("1.0", END).strip()
    result_label.config(text = " Hello, " + name +   + " Age:  "  + age + " Hobby: " + hobby + " About: " + about)

submit = Button(form_frame, text = "show my info" , bg = "purple", fg = "white", font = ("Arial", 11, "bold"), command = show_info)
submit.grid(row = 5, column = 0, columnspan=2, pady = 15)
            
result_label = Label(form_frame, text="Your info will appear here.", bg = "lightyellow",fg = "black", width = 35, height = 4, wraplength = 300, justify = "left")
result_label.grid(row = 6, column = 0, columnspan=2, pady = 10)
window.mainloop()


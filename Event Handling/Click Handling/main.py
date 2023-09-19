from customtkinter import *

app = CTk()
app.geometry("500x400")

def click_handler():
    print("Button Clicked")
    

btn = CTkButton(master=app, text="Click Me", command=click_handler)

btn.place(relx=0.5, rely=0.5, anchor="center") 


app.mainloop()
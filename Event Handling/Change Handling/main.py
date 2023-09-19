from customtkinter import *

app = CTk()
app.geometry("500x400")

def change_handler(value):
    print(f"Selected Value {value}")
    

btn = CTkSlider(master=app, from_=0, to=100, command=change_handler)

btn.place(relx=0.5, rely=0.5, anchor="center") 


app.mainloop()
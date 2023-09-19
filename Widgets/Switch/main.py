from customtkinter import *

app = CTk()
app.geometry("500x400")

switch = CTkSwitch(master=app, text="Option")

switch.place(relx=0.5, rely=0.5, anchor="center") 


app.mainloop()
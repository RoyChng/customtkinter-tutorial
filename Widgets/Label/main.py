from customtkinter import *

app = CTk()
app.geometry("500x400")

label = CTkLabel(master=app, text="Some Text...", font=("Arial", 20), text_color="#FFCC70")

label.place(relx=0.5, rely=0.5, anchor="center") 


app.mainloop()
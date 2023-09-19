from customtkinter import *

app = CTk()
app.geometry("500x400")

checkbox = CTkCheckBox(master=app, text="Option", fg_color="#C850C0", checkbox_height=30, 
                       checkbox_width=30, corner_radius=36)

checkbox.place(relx=0.5, rely=0.5, anchor="center") 


app.mainloop()
from customtkinter import *

app = CTk()
app.geometry("500x400")

textbox = CTkTextbox(master=app, scrollbar_button_color="#FFCC70", corner_radius=16,
                     border_color="#FFCC70", border_width=2)

textbox.place(relx=0.5, rely=0.5, anchor="center") 


app.mainloop()
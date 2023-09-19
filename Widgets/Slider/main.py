from customtkinter import *

app = CTk()
app.geometry("500x400")

slider = CTkSlider(master=app, from_=0, to=100, number_of_steps=5,
                   button_color="#C850C0", orientation="vertical")

slider.place(relx=0.5, rely=0.5, anchor="center") 


app.mainloop()
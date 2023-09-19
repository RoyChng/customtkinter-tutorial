from customtkinter import *

app = CTk()
app.geometry("500x400")

entry = CTkEntry(master=app, placeholder_text="Start typing...", width=300,
                text_color="#FFCC70")

entry.place(relx=0.5, rely=0.5, anchor="center") 


app.mainloop()
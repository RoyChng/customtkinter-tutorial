from customtkinter import *

app = CTk()
app.geometry("500x400")

count = 0

def click_handler():
    global count
    count += 1
    label.configure(text=f"You've clicked the button {count} times")


label = CTkLabel(master=app, text="You've clicked the button 0 times")
btn = CTkButton(master=app, text="Click Me", command=click_handler)

label.pack(anchor="s", expand=True, pady=10)
btn.pack(anchor="n", expand=True,)

app.mainloop()
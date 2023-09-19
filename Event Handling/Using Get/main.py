from customtkinter import *

app = CTk()
app.geometry("500x400")


def click_handler():
    print(f"Entered Value: {entry.get()}")


entry = CTkEntry(master=app, placeholder_text="Type anything...")
btn = CTkButton(master=app, text="Submit", command=click_handler)

entry.pack(anchor="s", expand=True, pady=10)
btn.pack(anchor="n", expand=True,)

app.mainloop()
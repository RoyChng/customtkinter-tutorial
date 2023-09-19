from customtkinter import *

app = CTk()
app.geometry("500x400")


tabview = CTkTabview(master=app)
tabview.pack(padx=20, pady=20)

tabview.add("Tab 1")
tabview.add("Tab 2")
tabview.add("Tab 3")

label_1 = CTkLabel(master=tabview.tab("Tab 1"), text="This is tab 1")
label_1.pack(padx=20, pady=20)

label_2 = CTkLabel(master=tabview.tab("Tab 2"), text="This is tab 2")
label_2.pack(padx=20, pady=20)

label_3 = CTkLabel(master=tabview.tab("Tab 3"), text="This is tab 3")
label_3.pack(padx=20, pady=20)

app.mainloop()
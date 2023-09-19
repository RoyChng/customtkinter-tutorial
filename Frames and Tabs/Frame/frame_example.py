from customtkinter import *

app = CTk()
app.geometry("900x600")

frame_2 = CTkFrame(master=app, fg_color="#606190")
frame_2.grid(row=0, column=1, padx=50, pady=50)

CTkLabel(master=frame_2, text="Section 2", font=("Arial Bold", 20), justify="left").pack(expand=True, pady=(30, 15))
CTkRadioButton(master=frame_2, text="Setting 1", fg_color="#ffffff", border_color="#ffffff").pack(expand=True, side="left", padx=20, pady=(20, 50))
CTkRadioButton(master=frame_2, text="Setting 2", fg_color="#ffffff", border_color="#ffffff").pack(expand=True, side="left", padx=20, pady=(20, 50))
CTkRadioButton(master=frame_2, text="Setting 3", fg_color="#ffffff", border_color="#ffffff").pack(expand=True, side="left", padx=20, pady=(20, 50))

frame_3 = CTkFrame(master=app, fg_color="#4EAC7D")
frame_3.grid(row=1, column=1)

CTkLabel(master=frame_3, text="Section 3", font=("Arial Bold", 20), justify="left").pack(expand=True, pady=(30, 15))
CTkEntry(master=frame_3, placeholder_text="Enter your username", width=400).pack(expand=True, pady=15, padx=20)
CTkEntry(master=frame_3, placeholder_text="Enter your password", width=400).pack(expand=True, pady=15, padx=20)
CTkButton(master=frame_3, text="Login").pack(expand=True, fill="both", pady=(30, 15), padx=30)


frame_1 = CTkScrollableFrame(master=app, fg_color="#CD8C67")
frame_1.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=50, pady=50)

CTkLabel(master=frame_1, text="Section 1", font=("Arial Bold", 20), justify="left").pack(expand=True, pady=[10, 30])
CTkCheckBox(master=frame_1, text="Option 1", border_color="#ffffff", fg_color="#ffffff", checkmark_color="#CD8C67").pack(expand=True, pady=20)
CTkCheckBox(master=frame_1, text="Option 2", border_color="#ffffff", fg_color="#ffffff", checkmark_color="#CD8C67").pack(expand=True, pady=20)
CTkCheckBox(master=frame_1, text="Option 3", border_color="#ffffff", fg_color="#ffffff", checkmark_color="#CD8C67").pack(expand=True, pady=20)
CTkCheckBox(master=frame_1, text="Option 4", border_color="#ffffff", fg_color="#ffffff", checkmark_color="#CD8C67").pack(expand=True, pady=20)
CTkCheckBox(master=frame_1, text="Option 5", border_color="#ffffff", fg_color="#ffffff", checkmark_color="#CD8C67").pack(expand=True, pady=20)
CTkCheckBox(master=frame_1, text="Option 6", border_color="#ffffff", fg_color="#ffffff", checkmark_color="#CD8C67").pack(expand=True, pady=20)
CTkCheckBox(master=frame_1, text="Option 7", border_color="#ffffff", fg_color="#ffffff", checkmark_color="#CD8C67").pack(expand=True, pady=20)


app.mainloop()
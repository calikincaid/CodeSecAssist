import customtkinter
from customtkinter import *

def open_file_dialog():
    filename = filedialog.askopenfilename(
        filetypes=[("All files", "*.*"), ("Python files", "*.py")]
    )
    print("Selected file:", filename)
    return filename

set_appearance_mode("Dark")
set_default_color_theme("blue")

selected_file = open_file_dialog()
app = customtkinter.CTk()
app.mainloop()
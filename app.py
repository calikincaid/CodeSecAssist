import customtkinter as ctk
from main import PromptCrafter, QueryLLM, CodeSecAssistant


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Instance Variables
        self.filename = None

        #================================================================#
        # Creates the window
        self.geometry(f"{1200}x{600}")
        self.title("Code Security Assistant")

        # Creates the grid for the layout of the app
        self.grid_columnconfigure((0), weight=0)
        self.grid_columnconfigure((1, 2, 3, 4, 5, 6), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        #================================================================#

        #================================================================#
        # Create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, 
                                       text='''
┏┓   ┓  ┏┓       
┃ ┏┓┏┫┏┓┗┓┏┓┏
┗┛┗┛┗┻┗ ┗┛┗ ┗
┏┓  •
┣┫┏┏┓┏╋┏┓┏┓╋
┛┗┛┛┗┛┗┗┻┛┗┗    
''', 
                                       justify="left",
                                       font=ctk.CTkFont(family="Courier New", size=18, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=5, pady=(10, 5))
        
        # Creates the tutorial button within the sidebar frame
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Tutorial")
        self.sidebar_button_1.grid(row=1, column=0, padx=5, pady=10)
        
        # Creates the appearance option menu within the sidebar frame
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=5, pady=(10, 10))
        
        # Creates the scaling option menu within the sidebar frame       
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"], command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=5, pady=(10, 20))

        # Creates response textbox
        self.response_textbox = ctk.CTkTextbox(self, width=600, height=450, fg_color="transparent", state="disabled", wrap="word") 
        self.response_textbox.grid(row=0, column=1, columnspan=5, rowspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")
        #================================================================#


        #================================================================#
        # Create source_code frame with entry and buttons
        self.source_code_frame = ctk.CTkFrame(self, width=100)
        self.source_code_frame.grid(row=3, column=1, columnspan=4, padx=(20, 20), pady=(20, 20), sticky="new")
        self.source_code_frame.grid_columnconfigure(0, weight=6)
        self.source_code_frame.grid_columnconfigure(1, weight=1)
        self.source_code_frame.grid_columnconfigure(2, weight=1)

        self.source_label = ctk.CTkLabel(self.source_code_frame, 
                                       text="Upload Source Code",
                                       justify="left",
                                       font=ctk.CTkFont(family="Courier New", size=18, weight="bold"))
        self.source_label.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="w")

        # Creates the browse button for selecting source code file
        self.browse_button = ctk.CTkButton(self.source_code_frame, 
                                    command = self.open_file_dialog, 
                                    text = "Browse", 
                                    hover_color = "darkgray", 
                                    fg_color ="gray",
                                    border_width=2,
                                    text_color = "white"
                                    )
        self.browse_button.grid(row=3, column=2, padx=20, pady=20, sticky="nsew")

        # create main entry and button
        self.entry = ctk.CTkEntry(self.source_code_frame, width=500, placeholder_text="Enter source code here or browse for file.")
        self.entry.grid(row=3, column=0, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.submit_button = ctk.CTkButton(self.source_code_frame, text="Submit", fg_color="gray", border_width=2, hover_color="darkgray", text_color=("white", "white"))
        self.submit_button.grid(row=3, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        #================================================================#

        #================================================================#
        # Create the Start Analysis button
        self.analyse_button = ctk.CTkButton(self, 
                                    command = self.analyze_button_event, 
                                    text = f"START\nANALYSIS", 
                                    hover_color = "darkgray", 
                                    fg_color ="gray",
                                    border_width=2,
                                    text_color = "white"
                                    )
        self.analyse_button.grid(row=3, column=5, padx=20, pady=20, sticky="nsew")
        #================================================================#

        #================================================================#
        # Create setttings frame with tabs and options
        self.settings_frame = ctk.CTkFrame(self, width=100)
        self.settings_frame.grid(row=0, column=7, rowspan=4, padx=20, pady=20, sticky="nsew")
        self.settings_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.logo_label = ctk.CTkLabel(self.settings_frame, 
                                       text="Settings",
                                       justify="center",
                                       font=ctk.CTkFont(family="Courier New", size=18, weight="bold"))
        self.logo_label.grid(row=0, column=7, sticky="n")
        #================================================================#

    def open_file_dialog(self):
        self.filename = ctk.filedialog.askopenfilename( filetypes = [("All files", "*.*")])
        print("Selected file:", self.filename)
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def analyze_button_event(self):
        self.response_textbox.delete("1.0", "end")
        assistant = CodeSecAssistant()
        response = assistant.run_GUI(self.filename) # needs error handling for if filename hasnt been populated yet 
        self.response_textbox.configure(state="normal")

        for item in response:
            self.response_textbox.insert("end", f"{item}\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()



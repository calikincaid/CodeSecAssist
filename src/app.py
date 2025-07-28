import customtkinter as ctk
from main import PromptCrafter, QueryLLM, CodeSecAssistant

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Instance Variables
        self.source = None
        self.llm_selection = "Gemini"

        #================================================================#
        # Creates the window
        self.geometry(f"{1200}x{600}")
        self.title("Code Security Assistant")

        # Creates the grid for the layout of the app
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1, 2, 3, 4, 5, 6), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        #================================================================#

        #================================================================#
        # Create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text=f"CodeSec\nAssistant", justify="left", font=ctk.CTkFont(family="Courier New", size=36, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=5, pady=(10, 5))
        
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
        self.response_textbox = ctk.CTkTextbox(self, width=600, height=450, fg_color="transparent", state="disabled", wrap="word", font=ctk.CTkFont( size=18, weight="bold")) 
        self.response_textbox.grid(row=0, column=1, columnspan=5, rowspan=3, padx=20, pady=20, sticky="nsew")
        #================================================================#

        #================================================================#
        # Create source_code frame with entry and buttons
        self.source_code_frame = ctk.CTkFrame(self, width=100)
        self.source_code_frame.grid(row=3, column=1, columnspan=4, padx=20, pady=20, sticky="nsew")
        self.source_code_frame.grid_columnconfigure(0, weight=6)
        self.source_code_frame.grid_columnconfigure(1, weight=1)
        self.source_code_frame.grid_columnconfigure(2, weight=1)

        # Creates the source_code frame label
        self.source_label = ctk.CTkLabel(self.source_code_frame, text="Upload Source Code", justify="left", font=ctk.CTkFont(size=14))
        self.source_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Creates the browse button for selecting source code file
        self.browse_button = ctk.CTkButton(self.source_code_frame, text="Browse", text_color="white", command=self.open_file_dialog)
        self.browse_button.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        # Create main entry and button
        self.entry = ctk.CTkEntry(self.source_code_frame, width=500, placeholder_text="Enter source code here or browse for file.")
        self.entry.grid(row=3, column=0, padx=10, pady=10, sticky="new")

        self.submit_button = ctk.CTkButton(self.source_code_frame, text="Submit", text_color="white", command=self.source_submit_button_event)
        self.submit_button.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")
        #================================================================#

        #================================================================#
        # Create the Start Analysis button
        self.analyse_button = ctk.CTkButton(self, text=f"Start\nAnalysis", text_color="white", command=self.analyze_button_event)
        self.analyse_button.grid(row=3, column=5, padx=20, pady=20, sticky="nsew")
        #================================================================#

        #================================================================#
        # Create settings frame with tabs and options
        self.settings_frame = ctk.CTkFrame(self, width=100, corner_radius=20)
        self.settings_frame.grid(row=0, column=7, rowspan=4, padx=20, pady=20, sticky="nsew")
        self.settings_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.settings_label = ctk.CTkLabel(self.settings_frame, text="Settings", justify="center", font=ctk.CTkFont(family="Courier New", size=18, weight="bold"))
        self.settings_label.grid(row=0, column=7, sticky="nsew")
        
        # Creates the export to pdf frame and switch within the settings frame
        self.switch_frame = ctk.CTkFrame(self.settings_frame, width=100)
        self.switch_frame.grid(row=1, column=7, padx=20, pady=20, sticky="nsew")
        self.switch_frame.grid_rowconfigure((0,1), weight=1)
        self.switch_frame.grid_columnconfigure(0, weight=1)

        self.output_label = ctk.CTkLabel(self.switch_frame, text="Output .pdf", justify="center")
        self.output_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.output_switch = ctk.CTkSwitch(self.switch_frame, text="off | on", variable=ctk.StringVar(value="off"), onvalue="on", offvalue="off", state="disabled", command=self.output_selection_event)
        self.output_switch.grid(row=1, column=0, padx=5, pady=5)

        # Creates the LLM selection frame and dropdown within the settings frame
        self.llm_frame = ctk.CTkFrame(self.settings_frame, width=100)
        self.llm_frame.grid(row=7, column=7, padx=20, pady=20, sticky="nsew")
        
        # Creates the llm model option menu within the settings frame       
        self.llm_label = ctk.CTkLabel(self.llm_frame, text="LLM Model", anchor="w")
        self.llm_label.grid(row=0, column=0, padx=5, pady=5)
        self.llm_option_menu = ctk.CTkOptionMenu(self.llm_frame, values=["Gemini", "ChatGPT"], state="enabled", command=self.llm_option_menu_event) 
        self.llm_option_menu.grid(row=1, column=0, padx=5, pady=5)

        # Creates the source code option menu within the settings frame       
        self.code_label = ctk.CTkLabel(self.llm_frame, text="Source Code", anchor="w")
        self.code_label.grid(row=2, column=0, padx=5, pady=5)
        self.code_option_menu = ctk.CTkOptionMenu(self.llm_frame, values=["Python", "Java", "C++"], state="disabled", command=self.code_option_menu_event) 
        self.code_option_menu.grid(row=3, column=0, padx=5, pady=5)

        # Creates the prompt template  option menu within the settings frame       
        self.prompt_label = ctk.CTkLabel(self.llm_frame, text="Prompt Template", anchor="w")
        self.prompt_label.grid(row=4, column=0, padx=5, pady=5)
        self.prompt_option_menu = ctk.CTkOptionMenu(self.llm_frame, values=["Detect Owasp Vulns", "PROMPT_OPTION", "PROMPT_OPTION"], state="disabled", command=self.prompt_option_menu_event) 
        self.prompt_option_menu.grid(row=5, column=0, padx=5, pady=5)

        # Creates the output language option menu within the settings frame       
        self.language_label = ctk.CTkLabel(self.llm_frame, text="Output Language", anchor="w")
        self.language_label.grid(row=6, column=0, padx=5, pady=5)
        self.language_option_menu = ctk.CTkOptionMenu(self.llm_frame, values=["English", "Español", "Deutsch"], state="disabled", command=self.language_option_menu_event) 
        self.language_option_menu.grid(row=7, column=0, padx=5, pady=5)
        #================================================================#
  
    ###################### BUTTON ACTIONS ######################
    def open_file_dialog(self):
        self.source = ctk.filedialog.askopenfilename( filetypes = [("All files", "*.*")])
        print("Selected file:", self.source)
        
    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def analyze_button_event(self):
        self.response_textbox.delete("1.0", "end")
        assistant = CodeSecAssistant()
        response = assistant.run_GUI(self.source, self.llm_selection) # needs error handling for if source hasnt been populated yet 
        self.response_textbox.configure(state="normal")

        for vulnerability in response:
            self.response_textbox.insert("end", f"{vulnerability}\n")

    def source_submit_button_event(self):
        self.source = self.entry.get()
        self.entry.delete(0, "end")
        print("Submitted source code.")

    def llm_option_menu_event(self, choice):
        self.llm_selection = choice
        print(f"Configured LLM selection: {choice}")
        pass

    def code_option_menu_event(self):
        pass
    
    def prompt_option_menu_event(self):
        pass

    def language_option_menu_event(self):
        pass

    def output_selection_event(self):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()
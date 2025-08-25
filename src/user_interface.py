import customtkinter as ctk
import darkdetect
import tkinter as tk

class ZypherApp:
    def __init__(self, download_callback, format_callback, icon_path, custom_folder):
        self.custom_folder = custom_folder
        self.download_callback = download_callback
        self.format_callback = format_callback

        # Initialize CustomTkinter
        theme = "Dark" if darkdetect.isDark() else "Light"
        ctk.set_appearance_mode(theme)
        ctk.set_default_color_theme("dark-blue")

        self.window = ctk.CTk()
        self.window.title("Zypher - Lite")
        self.window.geometry("400x500")
        self.window.resizable(False, False)

        try:
            self.window.iconbitmap(icon_path)
        except Exception as e:
            print(f"Failed to load icon: {e}")

        self.label = ctk.CTkLabel(self.window, text="Zypher Lite", font=("Arial Black", 25, "bold"))
        self.label.pack(pady=20)

        self.info_label = ctk.CTkLabel(
            self.window, 
            text="No FFmpeg • Native formats only", 
            font=("Arial", 10), 
            text_color="gray"
        )
        self.info_label.pack(pady=(0, 10))

        self.textbox = ctk.CTkTextbox(self.window, height=100, width=300)
        self.textbox.pack(pady=10)

        self.status_frame = ctk.CTkFrame(self.window, fg_color="transparent", width=300, height=50)
        self.status_frame.pack(pady=10)
        self.status_frame.pack_propagate(False)

        self.text_frame = ctk.CTkFrame(self.status_frame, fg_color="transparent", height=30)
        self.text_frame.pack(pady=(0, 5))
        self.text_frame.pack_propagate(False)

        self.feedback_label = ctk.CTkLabel(self.text_frame, text="", font=("Arial", 12), wraplength=300, justify="center")
        self.feedback_label.pack()

        self.download_button = ctk.CTkButton(self.window, text="Download", command=self.start_download)
        self.download_button.pack(pady=2)

        self.folder_button = ctk.CTkButton(self.window, text="Change Download Folder", command=self.custom_folder)
        self.folder_button.pack(pady=20)

        self.format_switch = ctk.CTkSwitch(
            self.window, 
            text="Video / Audio (native)", 
            command=self.format_callback
        )
        self.format_switch.pack(pady=5)

        self.theme_switch = ctk.CTkSwitch(self.window, text="Change Theme", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def update_feedback(self, message, color):
        self.feedback_label.configure(text=message, text_color=color)

    def start_download(self):
        box_content = self.textbox.get("1.0", "end-1c")
        lines = box_content.split("\n")
        urls = []
        for line in lines:
            Clean_line = line.strip() # Clean the line
            if Clean_line:  # Verify if have something
                urls.append(Clean_line)  # Add to the list
        self.download_callback(urls, self)

    def toggle_theme(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)

    def run(self):
        self.window.mainloop()
import customtkinter as ctk
import tkinter as tk

class ZypherApp:
    def __init__(self, download_callback, format_callback, icon_path, custom_folder):
        self.custom_folder = custom_folder
        self.download_callback = download_callback
        self.format_callback = format_callback

        # Initialize CustomTkinter
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("dark-blue")

        # Create the main window
        self.window = ctk.CTk()
        self.window.title("Zypher")
        self.window.geometry("400x400")
        self.window.resizable(False, False)

        try:
            self.window.iconbitmap(icon_path)
        except Exception as e:
            print(f"Failed to load icon: {e}")

        # Main label
        self.label = ctk.CTkLabel(self.window, text="Zypher", font=("Arial Black", 25, "bold"))
        self.label.pack(pady=20)

        # Text entry
        self.entry = ctk.CTkEntry(self.window, placeholder_text="Insert video link here", width=300)
        self.entry.pack(pady=10)

        # Status frame for feedback and progress bar
        self.status_frame = ctk.CTkFrame(self.window, fg_color="transparent", width=300, height=70)
        self.status_frame.pack(pady=10)
        self.status_frame.pack_propagate(False)

        # Progress bar
        self.progress_bar = ctk.CTkProgressBar(self.status_frame, mode="indeterminate", width=200)
        self.progress_bar.set(0)

        # Feedback label
        self.feedback_label = ctk.CTkLabel(self.status_frame, text="", font=("Arial", 12), wraplength=300, justify="center")
        self.feedback_label.pack(pady=10)

        # Download button
        self.download_button = ctk.CTkButton(self.window, text="Download", command=self.start_download)
        self.download_button.pack(pady=2)

        #Folder Location
        self.folder_button = ctk.CTkButton(self.window, text="Change Download Folder", command=self.custom_folder)
        self.folder_button.pack(pady=20)

        # Format switch
        self.format_switch = ctk.CTkSwitch(self.window, text="Video/Audio", command=self.format_callback)
        self.format_switch.pack(pady=5)

        # Theme switch
        self.theme_switch = ctk.CTkSwitch(self.window, text="Light/Dark Mode", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def start_loading(self):
        self.progress_bar.pack(in_=self.status_frame, pady=10)
        self.progress_bar.start()
        self.feedback_label.pack_forget()

    def stop_loading(self):
        self.progress_bar.stop()
        self.progress_bar.pack_forget()
        self.feedback_label.pack(in_=self.status_frame, pady=10)

    def update_feedback(self, message, color):
        self.feedback_label.configure(text=message, text_color=color)

    def start_download(self):
        self.download_callback(self.entry.get(), self)

    def toggle_theme(self):
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)

    def run(self):
        self.window.mainloop()

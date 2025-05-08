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

        # Create the main window
        self.window = ctk.CTk()
        self.window.title("Zypher")
        self.window.geometry("400x450")  # Increased height for log
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

        # Progress bar (now determinate)
        self.progress_bar = ctk.CTkProgressBar(self.status_frame, width=300)
        self.progress_bar.set(0)  # Start at 0%

        # Feedback label
        self.feedback_label = ctk.CTkLabel(self.status_frame, text="", font=("Arial", 12), wraplength=300, justify="center")
        self.feedback_label.pack(pady=10)

        # Log text area (minimal terminal)
        self.log_frame = ctk.CTkFrame(self.window, fg_color="transparent", width=300, height=50)
        self.log_frame.pack(pady=5)
        self.log_frame.pack_propagate(False)
        
        self.log_text = ctk.CTkLabel(
            self.log_frame, 
            text="", 
            font=("Consolas", 10),
            wraplength=300,
            justify="left",
            anchor="w"
        )
        self.log_text.pack(fill="both", expand=True)

        # Download button
        self.download_button = ctk.CTkButton(self.window, text="Download", command=self.start_download)
        self.download_button.pack(pady=2)

        # Folder Location
        self.folder_button = ctk.CTkButton(self.window, text="Change Download Folder", command=self.custom_folder)
        self.folder_button.pack(pady=10)

        # Format switch
        self.format_switch = ctk.CTkSwitch(self.window, text="Video/Audio", command=self.format_callback)
        self.format_switch.pack(pady=5)

        # Theme switch
        self.theme_switch = ctk.CTkSwitch(self.window, text="Change Theme", command=self.toggle_theme)
        self.theme_switch.pack(pady=10)

    def start_loading(self):
        """Start loading animation with determinate progress bar set to 0"""
        self.progress_bar.pack(in_=self.status_frame, pady=10)
        self.progress_bar.set(0)  # Reset to 0%
        self.feedback_label.pack_forget()
        self.log_text.configure(text="Starting download...")

    def stop_loading(self):
        """Stop loading animation and hide progress bar"""
        self.progress_bar.pack_forget()
        self.feedback_label.pack(in_=self.status_frame, pady=10)

    def update_progress(self, progress_value):
        """Update progress bar with a specific value (0-1)"""
        if 0 <= progress_value <= 1:
            self.progress_bar.set(progress_value)
            self.window.update_idletasks()  # Force GUI update

    def update_log(self, message):
        """Update the log text area with status information"""
        self.log_text.configure(text=message)
        self.window.update_idletasks()  # Force GUI update

    def update_feedback(self, message, color):
        """Update the feedback label with a colored message"""
        self.feedback_label.configure(text=message, text_color=color)
        self.window.update_idletasks()  # Force GUI update

    def start_download(self):
        """Start the download process using the provided callback"""
        self.download_callback(self.entry.get(), self)

    def toggle_theme(self):
        """Toggle between light and dark themes"""
        current_mode = ctk.get_appearance_mode()
        new_mode = "Light" if current_mode == "Dark" else "Dark"
        ctk.set_appearance_mode(new_mode)

    def run(self):
        """Start the application main loop"""
        self.window.mainloop()
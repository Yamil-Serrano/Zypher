import os
import tkinter as tk
from pathlib import Path
import customtkinter as ctk
from yt_dlp import YoutubeDL
import threading

# Downloads folder
download_folder = str(Path.home() / "Downloads")

def start_loading_animation():
    """Start the loading animation."""
    progress_bar.pack(in_=status_frame, pady=10)  # Show progress bar
    progress_bar.start()  # Start animation
    feedback_label.pack_forget()  # Hide feedback label

def stop_loading_animation():
    """Stop the loading animation."""
    progress_bar.stop()  # Stop animation
    progress_bar.pack_forget()  # Hide progress bar
    feedback_label.pack(in_=status_frame, pady=10)  # Show feedback label

def videodownloader(link):
    """Download video from the provided link."""
    if not link:
        feedback_label.configure(text="Please enter a link.", text_color="red")  # Show error if no link
        return
    
    def download_thread():
        """Download video in a separate thread."""
        start_loading_animation()  # Start loading animation
        
        options = {
            'format': 'best',  # Download the best quality
            'noplaylist': True,  # Do not download playlists
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s')  # Output file template
        }

        try:
            with YoutubeDL(options) as ydl:
                ydl.download([link])  # Download video
            Window.after(0, lambda: feedback_label.configure(text="Downloaded\nCheck your Downloads folder."))  # Success message
        except Exception as e:
            Window.after(0, lambda: feedback_label.configure(text="Download error!\nWhat the heck did you enter?"))  # Error message
            print(f"Error: {e}")  # Log error
        finally:
            Window.after(0, stop_loading_animation)  # Stop loading animation regardless of outcome

    # Start download in a separate thread
    thread = threading.Thread(target=download_thread)
    thread.daemon = True  # Allow thread to exit when main program exits
    thread.start()  # Start the thread

def charcolor():
    """Return text color based on current theme."""
    return "white" if ctk.get_appearance_mode() == "Dark" else "black"

def toggle_theme():
    """Toggle between light and dark themes."""
    current_mode = ctk.get_appearance_mode()  # Get current theme mode
    new_mode = "Light" if current_mode == "Dark" else "Dark"
    ctk.set_appearance_mode(new_mode)  # Set new theme mode
    
    # Update text colors
    label.configure(text_color=charcolor())
    feedback_label.configure(text_color=charcolor())
    
    # Update the switch state inversely
    theme_switch.select() if new_mode == "Light" else theme_switch.deselect()

# Initialize CustomTkinter
ctk.set_appearance_mode("Light")  # Set initial appearance mode
ctk.set_default_color_theme("dark-blue")  # Set color theme

# Create the main window
Window = ctk.CTk()
Window.geometry("400x400")  # Set window size
Window.title("TubeLink")  # Set window title
Window.resizable(False, False)

# Main label
label = ctk.CTkLabel(
    Window, 
    text="TubeLink", 
    font=("Arial Black", 20, "bold"),  
    text_color=charcolor()  # Set text color based on theme
)
label.pack(pady=20)  # Add padding

# Text entry
entry = ctk.CTkEntry(Window, placeholder_text="Insert YouTube link here", width=300)
entry.pack(pady=10)  # Add padding

# Create a frame for status indicators (progress bar and feedback label)
status_frame = ctk.CTkFrame(Window, fg_color="transparent", height=50)
status_frame.pack(pady=10)
status_frame.pack_propagate(False)  # Prevent the frame from shrinking

# Progress bar (initially hidden)
progress_bar = ctk.CTkProgressBar(status_frame, mode="indeterminate", width=200)
progress_bar.set(0)  # Set initial value

# Feedback label
feedback_label = ctk.CTkLabel(status_frame, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

# Download button
button = ctk.CTkButton(Window, text="Download", command=lambda: videodownloader(entry.get()))
button.pack(pady=20)  # Add padding

# Create a switch to toggle between light and dark modes
theme_switch = ctk.CTkSwitch(Window, text="Light/Dark Mode", command=toggle_theme)
theme_switch.pack(pady=10)  # Add padding

# Initialize the switch state based on the current mode
theme_switch.select() if ctk.get_appearance_mode() == "Light" else theme_switch.deselect()

# Start the main loop
Window.mainloop()

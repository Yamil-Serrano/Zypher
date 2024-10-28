import os
import sys
import tkinter as tk
from pathlib import Path
import customtkinter as ctk
from yt_dlp import YoutubeDL
import threading

# Downloads folder
download_folder = str(Path.home() / "Downloads")
is_video = True

def changeformat():
    global is_video
    is_video = not is_video
    # El switch se moverá a la derecha cuando is_video sea False (audio)
    format_switch.deselect() if is_video else format_switch.select()

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

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
        global is_video
        start_loading_animation()  # Start loading animation
        
        options0 = {
            'format': 'best',  # Download the best quality
            'noplaylist': True,  # Do not download playlists
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s')  # Output file template
        }

        options1 = {
            'format': 'bestaudio[ext=m4a]/bestaudio[ext=webm]/best',  
            'noplaylist': True, 
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  
        }


        try:
            if is_video:
                with YoutubeDL(options0) as ydl:
                    ydl.download([link])  # Download video
            else:
                with YoutubeDL(options1) as ydl:
                    ydl.download([link])  # Download aundio

            Window.after(0, lambda: feedback_label.configure(text="Downloaded!\nCheck your Downloads folder."))  # Success message
        except Exception as e:
            Window.after(0, lambda: feedback_label.configure(text="Download error!\nWhat the heck did you enter?\nCheck your connection maybe thats the problem."))  # Error message
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
    
    # Update the switch state (izquierda Light, derecha Dark)
    theme_switch.deselect() if new_mode == "Light" else theme_switch.select()

# Initialize CustomTkinter
ctk.set_appearance_mode("Light")  # Set initial appearance mode
ctk.set_default_color_theme("dark-blue")  # Set color theme

# Create the main window
Window = ctk.CTk()
icon_path = resource_path("resources/video.ico")
try:
    Window.iconbitmap(icon_path)
except Exception as e:
    print(f"Failed to load icon: {e}")
    print(f"Attempted path: {icon_path}")
Window.geometry("400x400")  # Set window size
Window.title("LinkTube")  # Set window title
Window.resizable(False, False)

# Main label
label = ctk.CTkLabel(
    Window, 
    text="LinkTube", 
    font=("Arial Black", 20, "bold"),  
    text_color=charcolor()  # Set text color based on theme
)
label.pack(pady=20)  # Add padding

# Text entry
entry = ctk.CTkEntry(Window, placeholder_text="Insert YouTube link here", width=300)
entry.pack(pady=10)  # Add padding

# Create a frame for status indicators (progress bar and feedback label)
status_frame = ctk.CTkFrame(Window, fg_color="transparent", width=300, height=70)
status_frame.pack(pady=10)
status_frame.pack_propagate(False)  # Prevent the frame from shrinking

# Progress bar (initially hidden)
progress_bar = ctk.CTkProgressBar(status_frame, mode="indeterminate", width=200)
progress_bar.set(0)  # Set initial value

# Feedback label
feedback_label = ctk.CTkLabel(status_frame, text="", font=("Arial", 12), wraplength=300, justify="center")
feedback_label.pack(pady=10)

# Download button
button = ctk.CTkButton(Window, text="Download", command=lambda: videodownloader(entry.get()))
button.pack(pady=20)  # Add padding

# Create a switch to toggle between light and dark modes
theme_switch = ctk.CTkSwitch(Window, text="Light/Dark Mode", command=toggle_theme)
theme_switch.pack(pady=10)

format_switch = ctk.CTkSwitch(Window, text="Video/Audio", command=changeformat)
format_switch.pack(pady=10)

# Inicializar estados de los switches (ambos a la izquierda inicialmente)
theme_switch.deselect()  # Light mode (izquierda)
format_switch.deselect()  # Video mode (izquierda)

# Start the main loop
Window.mainloop()

#pyinstaller --onefile --noconsole --add-data "resources/video.ico;resources" main.py
#Use the previous line to generate a binary file (exe)
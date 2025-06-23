import os
import sys
from pathlib import Path
from tkinter import filedialog
from yt_dlp import YoutubeDL
import threading
from user_interface import ZypherApp

# Default Downloads folder
download_folder = str(Path.home() / "Downloads")
is_video = True

def changefolder():
    global download_folder
    download_folder = filedialog.askdirectory()

def changeformat():
    global is_video
    is_video = not is_video

def resource_path(relative_path):
    # Get absolute path to resource, works for dev and for PyInstaller
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def videodownloader(link, app):
    if not link:
        app.update_feedback("Please enter a link.", "red")
        return

    def download_thread():
        app.start_loading()
        
        if is_video:
            # Video download - native formats without conversion
            options = {
                'format': 'best[ext=mp4]/best[ext=webm]/best',
                'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
                'noplaylist': True,
                'nocheckcertificate': True,
            }
        else:
            # Audio download - native formats only
            options = {
                'format': 'bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio/best',
                'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
                'noplaylist': True,
                'nocheckcertificate': True,
            }

        try:
            with YoutubeDL(options) as ydl:
                ydl.download([link])
            
            format_type = "Video" if is_video else "Audio"
            app.update_feedback(f"{format_type} downloaded!\nCheck your Downloads folder.", "green")
        except Exception as e:
            error_msg = str(e).lower()
            if 'ffmpeg' in error_msg:
                app.update_feedback("Error: FFmpeg required for this format.\nTry video mode instead.", "red")
            else:
                app.update_feedback("Download error!\nCheck your connection or try video mode.", "red")
            print(f"Error: {e}")
        finally:
            app.stop_loading()

    thread = threading.Thread(target=download_thread)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    icon_path = resource_path("resources/video.ico")
    app = ZypherApp(videodownloader, changeformat, icon_path, changefolder)
    app.run()

# For compile the app only
# pyinstaller --onefile --windowed --icon=resources/video.ico --name "Zypher-Lite" main.py --add-data "resources/video.ico;resources"
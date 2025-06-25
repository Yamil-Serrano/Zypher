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
            # Video download settings (native formats without conversion)
            options = {
                'format': 'best[ext=mp4]/best[ext=webm]/best',
                # Output template: Short, predictable filename with video ID to avoid Windows path issues
                'outtmpl': os.path.join(download_folder, 'Zypher_video_%(id)s.%(ext)s'),
                # Force sanitized filenames (removes special chars/emojis)
                'restrictfilenames': True,
                # Skip playlist extraction (download single video only)
                'noplaylist': True,
                # Mimic Chrome browser to avoid Facebook bot detection
                'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'},
                # Increase timeout to 30s for slow connections or responses
                'socket_timeout': 30,
                # Retry up to 3 times on temporary failures
                'extract_retry': 3,
            }
        else:
            # Audio download settings (native formats only)
            options = {
                'format': 'bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio/best',
                # Output template for audio files
                'outtmpl': os.path.join(download_folder, 'Zypher_audio_%(id)s.%(ext)s'),
                'restrictfilenames': True,
                'noplaylist': True,
                'http_headers': {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'},
                'socket_timeout': 30,
                'extract_retry': 3,
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
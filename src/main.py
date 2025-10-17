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

def videodownloader(links, app):
    if not links:
        app.update_feedback("Please enter at least one link.", "red")
        return

    def download_thread():
        error_count = 0
        success_count = 0

        # Loop Through URLs
        for i, link in enumerate(links):

            app.update_feedback(f"Downloading {i+1} of {len(links)}...", "steelblue")
            app.window.update()
        
            if is_video:
                # Video download settings (native formats without conversion)
                options = {
                    # Updated format selection for better compatibility
                    'format': 'bv*[ext=mp4][vcodec^=avc]+ba[ext=m4a]/b[ext=mp4]/b',
                    # Output template: Short, predictable filename with video ID to avoid Windows path issues
                    'outtmpl': os.path.join(download_folder, 'Zypher_video_%(id)s.%(ext)s'),
                    # Force sanitized filenames (removes special chars/emojis)
                    'restrictfilenames': True,
                    # Skip playlist extraction (download single video only)
                    'noplaylist': True,
                    # Updated headers and settings
                    'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-us,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Upgrade-Insecure-Requests': '1',
                    },
                    # Increase timeout to 30s for slow connections or responses
                    'socket_timeout': 30,
                    # Retry up to 3 times on temporary failures
                    'extractor_retries': 3,
                    'fragment_retries': 10,
                    'skip_unavailable_fragments': True,
                    'nocheckcertificate': True,

                    'extractor_args': {
                        'youtube': {
                            'player_client': ['android', 'web'],
                        }
                    },
                }
            else:
                # Audio download settings (native formats only)
                options = {
                    # Updated format for better compatibility
                    'format': 'bestaudio/best',
                    # Output template for audio files
                    'outtmpl': os.path.join(download_folder, 'Zypher_audio_%(id)s.%(ext)s'),
                    'restrictfilenames': True,
                    'noplaylist': True,
                    # Updated headers
                    'http_headers': {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-us,en;q=0.5',
                    },
                    'socket_timeout': 30,
                    # Retry settings for current YouTube
                    'extractor_retries': 3,
                    'fragment_retries': 10,
                    'skip_unavailable_fragments': True,
                    'nocheckcertificate': True,

                    # Note: No extractor_args for audio - they force video formats
                }

            try:
                with YoutubeDL(options) as ydl:
                    ydl.download([link])
                
                success_count += 1
                format_type = "Video" if is_video else "Audio"
                app.update_feedback(f"{format_type} {i+1} of {len(links)} downloaded!", "springgreen")

            except Exception as e:
                error_count += 1
                print(f"Error: {e}") # debug only message
                continue

        if error_count == 0:
            app.update_feedback(f"All {success_count} downloads completed!", "springgreen")
        elif success_count > 0:
            app.update_feedback(f"⚠️ Completed: {success_count} success, {error_count} failed", "orange")
        else:
            app.update_feedback(f"⚠️ All downloads failed!", "red")

    thread = threading.Thread(target=download_thread)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    icon_path = resource_path("resources/video.ico")
    app = ZypherApp(videodownloader, changeformat, icon_path, changefolder)
    app.run()

# For compile the app only
# pyinstaller --onefile --windowed --icon=resources/video.ico --name "Zypher-Lite" main.py --add-data "resources/video.ico;resources"
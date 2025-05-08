import os
import sys
import time
import random
from pathlib import Path
from tkinter import filedialog
from yt_dlp import YoutubeDL
import threading
from user_interface import ZypherApp

# Default Downloads folder
download_folder = str(Path.home() / "Downloads")
is_video = True

def changefolder():
    """Change the folder where you'd like to save the video."""
    global download_folder
    folder = filedialog.askdirectory()
    if folder:  # If user doesn't cancel
        download_folder = folder

def changeformat():
    """Toggle between video and audio download formats."""
    global is_video
    is_video = not is_video

def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def videodownloader(link, app):
    """Download video or audio from the provided link."""
    if not link:
        app.update_feedback("Please enter a link.", "red")
        return

    def download_thread():
        """Download video in a separate thread."""
        app.start_loading()  # Start loading animation
        
        # Basic options configuration
        options = {
            'format': 'mp4' if is_video else 'bestaudio[ext=m4a]',
            'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
            'noplaylist': False,  # Always allow playlists
            'extract_audio': not is_video,
            'nocheckcertificate': True,
            'continuedl': False,  # Disable download continuation
            'noresizebuffer': True,
            'buffersize': 1024 * 16,
            'retries': 10,
            'fragment_retries': 10,
            'retry_sleep': 2,
            'socket_timeout': 30,
            'nopart': True,  # Don't save partial files to avoid locks
            'no_warnings': False,  # Show warnings
            'windowsfilenames': True,  # Use Windows-compatible filenames
            'ignoreerrors': True,  # Ignore errors and continue with the next video
        }

        # Callback to handle progress and messages
        def my_hook(d):
            if d['status'] == 'error':
                print(f"Error: {d.get('error')}")
                app.update_log(f"Error: {d.get('error', 'Unknown error')}")
                
            elif d['status'] == 'finished':
                filename = d['filename']
                app.update_feedback(f"Processing: {os.path.basename(filename)}", "blue")
                app.update_log(f"Processing: {os.path.basename(filename)}")
                app.update_progress(1.0)  # Set progress to 100% when finished
                
            elif d['status'] == 'downloading':
                # Update progress bar if total_bytes is available
                if 'total_bytes' in d and d['total_bytes'] > 0:
                    percent = d['downloaded_bytes'] / d['total_bytes'] 
                    app.update_progress(percent)  # Update progress bar (0-1)
                    
                    # Format speed nicely
                    speed = d.get('speed', 0)
                    if speed:
                        speed_str = f"{speed/1024:.1f} KB/s" if speed < 1024*1024 else f"{speed/1024/1024:.1f} MB/s"
                        
                        # Update both feedback and log
                        filename = os.path.basename(d.get('filename', '').split('/')[-1])
                        app.update_feedback(f"Downloading: {filename}\n{percent*100:.1f}% @ {speed_str}", "blue")
                        
                        # Update log with current file and ETA
                        eta = d.get('eta', 0)
                        eta_str = f"{eta}s" if eta < 60 else f"{eta//60}m {eta%60}s"
                        app.update_log(f"{filename} | {percent*100:.1f}% | {speed_str} | ETA: {eta_str}")
                
                # When total_bytes isn't available (some streams)
                elif 'downloaded_bytes' in d:
                    downloaded = d['downloaded_bytes'] / (1024 * 1024)  # MB
                    speed = d.get('speed', 0)
                    if speed:
                        speed_str = f"{speed/1024:.1f} KB/s" if speed < 1024*1024 else f"{speed/1024/1024:.1f} MB/s"
                        app.update_log(f"Downloaded: {downloaded:.1f}MB | {speed_str}")
                        # Use indeterminate progress in this case
                        app.update_progress(0.5)  # Show some progress
                
        options['progress_hooks'] = [my_hook]

        try:
            with YoutubeDL(options) as ydl:
                # First extract information to determine if it's a playlist
                app.update_log("Extracting video information...")
                info = ydl.extract_info(link, download=False)
                
                # Determine if it's a playlist
                is_playlist = 'entries' in info
                
                if is_playlist:
                    # It's a playlist
                    playlist_title = info.get('title', 'Playlist')
                    video_count = len(info['entries'])
                    app.update_feedback(f"Downloading playlist: {playlist_title}\n{video_count} videos", "blue")
                    app.update_log(f"Playlist: {playlist_title} ({video_count} videos)")
                
                # Download (either playlist or individual video)
                app.update_log("Starting download...")
                ydl.download([link])
                
                if is_playlist:
                    # Check how many were successfully downloaded
                    successful = sum(1 for entry in info['entries'] if entry is not None)
                    app.update_feedback(f"Completed!\n{successful}/{video_count} videos downloaded", "green")
                    app.update_log(f"Playlist complete: {successful}/{video_count} videos")
                else:
                    app.update_feedback("Download completed!\nCheck your Downloads folder.", "green")
                    app.update_log("Download complete!")
                
        except Exception as e:
            error_msg = str(e)
            if "WinError 32" in error_msg:
                # File in use - try with a random name
                try:
                    app.update_feedback("Filename in use. Retrying with another name...", "orange")
                    app.update_log("Filename in use. Retrying with random filename...")
                    options['outtmpl'] = os.path.join(download_folder, '%(title)s_' + str(random.randint(1000, 9999)) + '.%(ext)s')
                    with YoutubeDL(options) as ydl:
                        ydl.download([link])
                    app.update_feedback("Download completed!\nCheck your Downloads folder.", "green")
                    app.update_log("Download complete!")
                except Exception as retry_error:
                    app.update_feedback(f"Error: {str(retry_error)[:80]}...", "red")
                    app.update_log(f"Error: {str(retry_error)}")
            elif "416" in error_msg:
                # Error 416 - retry without continuing
                try:
                    app.update_feedback("Retrying download...", "orange")
                    app.update_log("Error 416. Retrying download...")
                    time.sleep(1)  # Small pause before retrying
                    with YoutubeDL(options) as ydl:
                        ydl.download([link])
                    app.update_feedback("Download completed!\nCheck your Downloads folder.", "green")
                    app.update_log("Download complete!")
                except Exception as retry_error:
                    app.update_feedback(f"Error: {str(retry_error)[:80]}...", "red")
                    app.update_log(f"Error: {str(retry_error)}")
            else:
                app.update_feedback(f"Error: {error_msg[:80]}...", "red")
                app.update_log(f"Error: {error_msg}")
                print(f"Full error: {e}")
        finally:
            app.stop_loading()  # Stop loading animation

    # Start the download in a separate thread
    thread = threading.Thread(target=download_thread)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    icon_path = resource_path("resources/video.ico")
    app = ZypherApp(videodownloader, changeformat, icon_path, changefolder)
    app.run()
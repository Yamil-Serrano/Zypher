# Zypher

**Zypher** is a modern and powerful video/audio downloader for Windows, designed with performance and flexibility in mind. Powered by the `yt_dlp` library, it gives you full control over format selection, quality settings, and media conversions.  
Simply copy the URL of the video you want to download, paste it into Zypher, and choose whether to download the video or extract the audio.

> **Note:** If a download fails, it's likely that the website you're trying to download from is not supported by `yt_dlp`.  
> You can check the list of supported websites in the official [GitHub repository](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md),  
> or by installing `yt_dlp` and running the following command:
>
> ```bash
> yt-dlp --list-extractors
> ```


##  Planned Features – Zypher (Full Version)

- **High-Quality Video Downloads**  
  Download videos in resolutions up to **1080p, 1440p, or 4K** depending on availability.

- **Format and Quality Selection**  
  Choose video/audio format and resolution before downloading.

- **FFmpeg Integration**  
  Advanced processing like merging video+audio, converting formats, and trimming clips.

- **Custom Settings**  
  Advanced download options, bitrate control, and batch processing.

- **Playlist and Channel Support**  
  Download full playlists or entire YouTube channels.

---

> ⚠️ **Note:** The full version of Zypher is currently **in development**. For now, you can use **Zypher Lite**, the stable and simplified version (see below).

---

# Zypher Lite

**Zypher Lite** is the stable, lightweight version of Zypher focused on simplicity and ease of use. It downloads audio and video using the native formats provided by the source without using FFmpeg. Ideal for quick downloads in standard quality.

---

## Features – Zypher Lite 

- **Native Format Downloads**  
  Downloads videos in `.mp4`, `.webm`, `.m4a`, etc., exactly as provided by YouTube.

- **Max 480p Video Resolution**  
  Downloads are limited to a maximum of 480p resolution for stability and speed.

- **Audio-Only Support**  
  Extract native audio without conversion (no `.mp3`).

- **No FFmpeg Needed**  
  Fast downloads with no extra tools or conversions.

- **Simple Interface**  
  Just paste your link, choose between video or audio, and download.

- **Custom Download Folder**  
  Choose where your downloads are saved.

---

## Screenshots – Zypher Lite
![image](https://github.com/user-attachments/assets/2c1a1c02-a5c2-4a95-859e-55084be11ea9)

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Yamil-Serrano/Zypher
   ```

2. Navigate to the project directory:
   ```bash
   cd Zypher
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Start the Application**
   ```bash
   python main.py
   ```

2. **Download a Video**
   - Paste a Video link in the text box
   - Select if you want Video or Audio
   - Click "Download"
   - The video will be saved in your Downloads folder
   - Use the Light/Dark Mode switch to toggle the theme

3. **View Downloads**
   - Downloaded videos or audios are saved to your system's Downloads folder by default

## Troubleshooting

### Common Issues and Solutions

1. **"Download error?"**
   - Ensure the link is a valid Video URL
   - Check if the video or audio is available in your region
   - Do you have internet connection?

2. **Progress bar stops or freezes**
   - If the download appears stuck:
     - Try restarting the app
     - Check your internet connection
     - Confirm yt-dlp is correctly installed

## 📝 License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](LICENSE.md).

## Contact

For any questions or suggestions, feel free to reach out:

GitHub: [Neowizen](https://github.com/Yamil-Serrano)

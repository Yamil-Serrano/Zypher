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

- **Batch Download Support**  
  Download multiple videos at once by pasting one URL per line in the text box.

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

- **Batch Download Support**  
  Download multiple videos at once by pasting one URL per line in the text box.
---

## Screenshots – Zypher Lite
<img width="821" height="807" alt="image" src="https://github.com/user-attachments/assets/19b5b674-d05d-403b-9a65-b428ac21156d" />

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

2. **Download Videos**
   - Paste one or multiple video links in the text box (one URL per line)
   - Select if you want Video or Audio mode
   - Click "Download"
   - All videos will be processed sequentially and saved to your Downloads folder

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

3. **Batch download issues**
   - If one download fails, the others will continue processing
   - Check the final summary for success/failure counts
   - Invalid URLs will be skipped automatically

## 📝 License

This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](LICENSE.md).

## Contact

For any questions or suggestions, feel free to reach out:

GitHub: [Neowizen](https://github.com/Yamil-Serrano)

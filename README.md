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

> ⚠️ **Note:** The full version of Zypher is currently **in development**. For now, you can use **Zypher Lite**, the stable and simplified version (see below).


# Zypher Lite

**Zypher Lite** is the stable, lightweight version of Zypher focused on simplicity and ease of use. It downloads audio and video using the native formats provided by the source without using FFmpeg. Ideal for quick downloads in standard quality.

Just paste one or multiple links (one URL per line), choose Video or Audio, and Zypher Lite will download them sequentially to your Downloads folder or to your custom folder if configured.

## Features – Zypher Lite 

- **Native Format Downloads**  
  Downloads videos in `.mp4`, `.webm`, `.m4a`, etc., exactly as provided by YouTube.

- **Limited video resolution**  
  Lower resolutions for speed and stability.

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

## Screenshots – Zypher Lite
<img width="821" height="807" alt="image" src="https://github.com/user-attachments/assets/19b5b674-d05d-403b-9a65-b428ac21156d" />


## Troubleshooting & Quick Fixes

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

If a download fails, **it may not be a permanent application error**. Websites like YouTube or Twitter change their structure frequently, and the version of `yt-dlp` bundled in the pre-compiled `.exe` file can become outdated over time.

**Try this quick fix:**

1.  **Update `yt-dlp` manually** in your Python environment:
    ```bash
    pip install --upgrade yt-dlp
    ```
2.  **Run Zypher from the source code:**
    - Make sure you have Python installed and have installed the requirements (`pip install -r requirements.txt`).
    - Run the application directly from your terminal.
    - This will use the **updated** version of `yt-dlp` on your system, which will likely resolve the download issue.

**Why does this work?**
The compiled version (`.exe`) contains a fixed version of `yt-dlp` from when it was created. Running from source code uses the most recent version of the library, which includes the latest patches for website changes and compatibility fixes.


## 📝 License
This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](LICENSE.md).

## Contact
If you have any questions or suggestions, feel free to reach out:
- **GitHub:** [Neowizen](https://github.com/Yamil-Serrano)

# Zypher Lite

**Zypher Lite** is a modern and lightweight video/audio downloader for Windows, focused on simplicity and ease of use. Powered by the `yt_dlp` library, it downloads audio and video using the native formats provided by the source.

Just paste one or multiple links (one URL per line), choose Video or Audio, and Zypher Lite will download them sequentially to your Downloads folder or to your custom folder if configured.

> **Note:** If a download fails, it's likely that the website you're trying to download from is not supported by `yt_dlp`.  
> You can check the list of supported websites in the official [GitHub repository](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md),  
> or by installing `yt_dlp` and running the following command:
>
> ```bash
> yt-dlp --list-extractors
> ```


## FFmpeg & Deno: Optional, Automatically Detected

Zypher Lite works out of the box with **no extra tools required**. By default, it downloads the native format returned directly by the source (usually `.mp4`, `.webm`, or `.m4a`), capped at a lower resolution for speed and stability.

However, Zypher Lite **automatically detects** whether FFmpeg and Deno are installed on your system. You don't need to configure anything just install them and Zypher Lite will pick them up on the next launch:

- **Without FFmpeg and Deno (default / Lite mode):** downloads are limited to the native, pre-merged format YouTube provides generally capped around **360p**.
- **With FFmpeg and Deno installed:** Zypher Lite unlocks full-quality downloads, merging the best available video and audio streams — typically **1080p or higher**, up to 4K depending on the source.

The app's interface tells you which mode is currently active, so you always know what to expect before downloading.

### How to Install FFmpeg and Deno

Both tools are free and take about a minute to install using `winget`, which comes built into Windows 10/11.

1. Open **PowerShell** (search for it in the Start menu).
2. Run the following commands:
   ```powershell
   winget install ffmpeg
   winget install DenoLand.Deno
   ```
3. **Close and reopen** PowerShell (and any other terminal, IDE, or Zypher Lite window you have open) this refreshes your system's PATH so the new tools can be found.
4. Verify both are installed correctly:
   ```powershell
   ffmpeg -version
   deno --version
   ```
   If each command prints a version number instead of an error, you're all set.
5. Launch Zypher Lite — the app checks for both tools automatically on startup and will switch to full-quality mode on its own.

## Features 

- **Native Format Downloads**  
  Downloads videos in `.mp4`, `.webm`, `.m4a`, etc., exactly as provided by YouTube.

- **Automatic Quality Scaling**  
  Detects FFmpeg and Deno on your system and automatically switches between Lite (native, lower-res) and full-quality (merged, high-res) downloads no manual setup required.

- **Audio-Only Support**  
  Extract audio in its native format by default (no `.mp3`); if FFmpeg is detected, audio is automatically converted to `.mp3` instead.

- **Simple Interface**  
  Just paste your link, choose between video or audio, and download.

- **Custom Download Folder**  
  Choose where your downloads are saved.

- **Batch Download Support**  
  Download multiple videos at once by pasting one URL per line in the text box.

## Screenshots
<img width="821" height="807" alt="image" src="https://github.com/user-attachments/assets/19b5b674-d05d-403b-9a65-b428ac21156d" />


## Troubleshooting & Quick Fixes

1. **"Download error?"**
   - Ensure the link is a valid Video URL
   - Check if the video or audio is available in your region
   - Do you have internet connection?

2. **Downloads are stuck at low resolution (360p)**
   - This is expected behavior in Lite mode. To unlock higher resolutions:
     - Install FFmpeg and Deno and make sure both are added to your system's PATH
     - Restart Zypher Lite — the app checks for both tools on launch and will switch to full-quality mode automatically
     - Verify both are installed correctly by running `ffmpeg -version` and `deno --version` in a terminal

3. **Progress bar stops or freezes**
   - If the download appears stuck:
     - Try restarting the app
     - Check your internet connection
     - Confirm yt-dlp is correctly installed

4. **Batch download issues**
   - If one download fails, the others will continue processing
   - Check the final summary for success/failure counts
   - Invalid URLs will be skipped automatically

If a download fails, **it may not be a permanent application error**. Websites like YouTube or Twitter change their structure frequently, and the version of `yt-dlp` bundled in the pre-compiled `.exe` file can become outdated over time.

**Try this quick fix:**

1.  **Update `yt-dlp` manually** in your Python environment:
    ```bash
    pip install --upgrade yt-dlp
    ```
2.  **Run Zypher Lite from the source code:**
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
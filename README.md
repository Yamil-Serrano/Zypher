# Zypher

A simple and user-friendly Video downloader built with Python. Zypher uses `yt-dlp` for handling video and audio downloads and `CustomTkinter` to provide a modern GUI with a light/dark mode toggle.

## Features

- **Download Best-Quality Videos**: Zypher downloads the best available quality for videos
- **Download Best-Quality Audios**: Zypher downloads the best audio quality available 
- **Simple Interface**: A clear and intuitive GUI to easily insert links and manage downloads
- **Loading Animation**: Progress bar animation for real-time download feedback
- **Theme Toggle**: Switch between light and dark modes to suit your preference

## Screenshots

![Screenshot 2024-11-08 211906](https://github.com/user-attachments/assets/099e3567-aeca-4040-9c71-3d0fa179e8db)


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

1. **"Download error! What the heck did you enter?"**
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

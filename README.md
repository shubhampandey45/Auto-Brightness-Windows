# 🌞 AutoBrightness  

[![Release](https://img.shields.io/github/v/release/YourUsername/AutoBrightness?style=for-the-badge)](https://github.com/YourUsername/AutoBrightness/releases)  
[![License](https://img.shields.io/github/license/YourUsername/AutoBrightness?style=for-the-badge)](./LICENSE)  

AutoBrightness is a **lightweight Python utility** that automatically adjusts your screen brightness in real-time based on your screen’s content brightness.  
No more eye strain while switching between bright and dark apps!  

---

## ✨ Features  
- 📸 Detects screen brightness using live snapshots  
- 🌗 Smooth brightness transitions (no flicker)  
- 🔄 Runs silently in the background  
- ⚙️ Customizable brightness range  

---

## 🚀 Installation  

### Option 1: Run the EXE (Recommended)  
1. Go to [**Releases**](https://github.com/YourUsername/AutoBrightness/releases)  
2. Download the latest `AutoBrightness.exe`  
3. Run it (**Admin required**)  

### Option 2: Run from Source  
Make sure you have **Python 3.9+** installed.  

```bash
git clone https://github.com/YourUsername/AutoBrightness.git
cd AutoBrightness
pip install -r requirements.txt
python content_auto_brightness.py
⚡ Usage
Once launched, AutoBrightness runs in the background and auto-adjusts brightness every few seconds.

To stop, simply close the program.

🔑 Requirements
Windows OS

Administrator privileges

📌 Roadmap / To-Do
 Add system tray icon with start/stop toggle

 Add user settings (update interval, brightness range)

 Cross-platform support (Linux/macOS if possible)

🛠️ Development
Main script: content_auto_brightness.py

Key libraries used:

mss (screenshot capture)

numpy (image processing)

screen-brightness-control (brightness control)

plyer (notifications)

📜 License
This project is licensed under the MIT License.

🤝 Contributing
Pull requests and suggestions are welcome!
If you’d like to improve features, fix bugs, or add enhancements, feel free to fork and open a PR.
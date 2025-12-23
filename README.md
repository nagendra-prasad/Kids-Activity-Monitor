# Kids Activity Monitor (Lightweight – Windows)

A **lightweight, low-resource Windows monitoring utility** designed for **parents and educators** to supervise kids’ learning and computer usage by periodically capturing screenshots.

This project focuses on:
- Minimal CPU & memory usage
- Transparency and ethics
- Simple, reliable operation

---

## ✨ Features

- Screenshot capture every **10 seconds**
- Very low CPU & RAM usage
- Dual-monitor support (captures monitor where cursor is active)
- JPG output (~80–120 KB per image)
- Date-wise folder structure
- Captures only when the user is active
- Auto-deletes screenshots older than 7 days
- JSON-based configuration
- Runs silently (no UI, no tray)
- Emergency stop mechanism (`STOP.MON`)
- Basic tamper resistance (no visible controls)

---

## 🖥 Supported Platform

- Windows 10 / Windows 11
- Python 3.9 or later

---

## 📦 Requirements

Install required dependencies:

```bash
pip install mss pillow

🚀 Getting Started

Clone the repository:

git clone https://github.com/yourusername/kids-activity-monitor.git
cd kids-activity-monitor

Run the application:

python kids_monitor_final.py

🧭 First Run Behavior

On the first run only, a folder selection dialog will appear

Select the folder where screenshots should be saved

The selected path is stored in a JSON config file:

C:\ProgramData\KidsMonitor\config.json


After this step:

No dialogs appear

The application runs completely in the background

⚙️ Configuration (JSON)
Config File Location
C:\ProgramData\KidsMonitor\config.json

Sample Configuration
{
  "save_path": "D:\\KidsScreens",
  "interval_seconds": 10,
  "retain_days": 7,
  "idle_seconds": 30
}

Configuration Options
Key	Description
save_path	Folder where screenshots are stored
interval_seconds	Screenshot interval (seconds)
retain_days	Number of days to keep screenshots
idle_seconds	Idle time before capture pauses
🗂 Folder Structure

Screenshots are automatically organized by date:

SaveFolder
 ├── 2025-12-23
 │   ├── 21-10-00.jpg
 │   ├── 21-10-10.jpg
 ├── 2025-12-24


This structure keeps storage clean and easy to review.

🛑 Stopping the Monitor

To stop the application safely, create a file named:

STOP.MON


inside the selected screenshot folder.

The application will detect this file and exit gracefully.

📊 Disk Usage Estimate

Assuming:

1 screenshot every 10 seconds

~100 KB per image

Duration	Approx Storage
1 Hour	~35 MB
24 Hours	~0.8 GB
7 Days	~5–6 GB

Actual usage may be lower due to idle-time detection.

🔐 Convert to Silent EXE (Optional)

Install PyInstaller:

pip install pyinstaller


Build command with embedded icon:

pyinstaller --onefile --noconsole --icon=kidsmonitor.ico kids_monitor_final.py


Output:

dist\KidsActivityService.exe


⚠️ Do not upload compiled EXE files to GitHub.

🎨 Icon Requirements

For best compatibility, the icon file should:

Be in .ico format

Contain multiple sizes:

16×16

32×32

48×48

256×256

⚠️ Legal & Ethical Notice

This tool is intended only for:

Parents monitoring their own children

Educational supervision on owned or authorized devices

Using this software without consent may be illegal.

The author assumes no responsibility for misuse.

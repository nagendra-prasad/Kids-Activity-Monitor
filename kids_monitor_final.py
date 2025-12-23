import os
import time
import json
import ctypes
from datetime import datetime, timedelta
import mss
from PIL import Image
import tkinter as tk
from tkinter import filedialog

# ===================== CONFIG =====================
CONFIG_DIR = r"C:\ProgramData\KDMonitor"
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

DEFAULT_CONFIG = {
    "save_path": "",
    "interval_seconds": 10,
    "retain_days": 7,
    "idle_seconds": 30
}
# =================================================


def load_config():
    os.makedirs(CONFIG_DIR, exist_ok=True)

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)

    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title="Select Folder to Save Screenshots")

    if not folder:
        raise SystemExit("No folder selected")

    config = DEFAULT_CONFIG.copy()
    config["save_path"] = folder

    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

    return config


def is_user_active(max_idle):
    class LASTINPUTINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_uint), ("dwTime", ctypes.c_uint)]

    lii = LASTINPUTINFO()
    lii.cbSize = ctypes.sizeof(lii)
    ctypes.windll.user32.GetLastInputInfo(ctypes.byref(lii))
    idle_time = (ctypes.windll.kernel32.GetTickCount() - lii.dwTime) / 1000
    return idle_time < max_idle


def get_cursor_monitor(sct):
    pt = ctypes.wintypes.POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pt))

    for monitor in sct.monitors[1:]:
        if (monitor["left"] <= pt.x <= monitor["left"] + monitor["width"] and
            monitor["top"] <= pt.y <= monitor["top"] + monitor["height"]):
            return monitor

    return sct.monitors[1]


def cleanup_old_folders(base_dir, keep_days):
    cutoff = datetime.now() - timedelta(days=keep_days)

    for folder in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder)
        if not os.path.isdir(folder_path):
            continue
        try:
            folder_date = datetime.strptime(folder, "%Y-%m-%d")
            if folder_date < cutoff:
                for f in os.listdir(folder_path):
                    os.remove(os.path.join(folder_path, f))
                os.rmdir(folder_path)
        except:
            pass


# ===================== MAIN =====================
config = load_config()

BASE_DIR = config["save_path"]
INTERVAL = config["interval_seconds"]
KEEP_DAYS = config["retain_days"]
IDLE_LIMIT = config["idle_seconds"]
STOP_FILE = os.path.join(BASE_DIR, "STOP.MON")

os.makedirs(BASE_DIR, exist_ok=True)
last_cleanup_day = datetime.now().date()

with mss.mss() as sct:
    while True:
        if os.path.exists(STOP_FILE):
            break

        if not is_user_active(IDLE_LIMIT):
            time.sleep(INTERVAL)
            continue

        today = datetime.now().strftime("%Y-%m-%d")
        day_dir = os.path.join(BASE_DIR, today)
        os.makedirs(day_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%H-%M-%S")
        png_path = os.path.join(day_dir, f"{timestamp}.png")
        jpg_path = os.path.join(day_dir, f"{timestamp}.jpg")

        monitor = get_cursor_monitor(sct)
        img = sct.grab(monitor)
        mss.tools.to_png(img.rgb, img.size, output=png_path)

        Image.open(png_path).convert("RGB").save(
            jpg_path, "JPEG", quality=60
        )
        os.remove(png_path)

        if datetime.now().date() != last_cleanup_day:
            cleanup_old_folders(BASE_DIR, KEEP_DAYS)
            last_cleanup_day = datetime.now().date()

        time.sleep(INTERVAL)

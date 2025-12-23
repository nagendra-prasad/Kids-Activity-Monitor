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

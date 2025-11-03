# Council Time Capsule - COE203 Python Project1

> **Personal Automation Tool**
> **Team:** [Esma ÜStün], [Orkun Bayraktar], [Onur Tayşun], [Taha Örnek], [Kava Başboğa]

---
## Project Overview

**Time Capsule** is a **real-time, future-unlocked message vault** that allows users to: 
- Write **personal messages** with **full datetime unlock** (year, month, day, hour, minute)
- **Optionally attach an image** using **Pillow (PIL)** - saved in 'capsule_images/'
- View **only unlocked messages** using 'datetime.datetime.now()'
- All data is **persistently stored** in 'capsule.txt'

> **W1-W4 Skills Used:**
> Functions
> Loops
> File I/O
> Lists
> 'datetime'
> 'os'
> Pillow
> Error Handling
> Input Validation

---

## Features

| Feature | Description |
| ------- | ----------- |
| **Add Message** | Enter text + full unlock datetime |
| **Attached Image (Optional)** | Uses 'Pilow' to verify & save image |
| **Real-Time Unlock** | 'datetime.datetime.now()' vs unlock time|
| **Presistent Storage** | 'capsule.txt' + 'capsule_images/' |
| **Input Validation** | Date in future, valid numbers |
| **Error Handling** | Invalid date, image error, file not found |
| **Auto Folder Creation** | 'capsule_images/' created if missing |

---

## File Structure

COUNCIL_TIME_CAPSULE/
│
├── time_capsule(project-1).py           # Main program (your code)
├── capsule.txt               # Messages stored here (auto-generated)
├── capsule_images/           # Saved images (e.g., image_20251103143025.jpg)
├── requirements.txt          # Pillow dependency
└── README.md                 # This file

---
## How to Run

```bash
git clone <https://github.com/ustunesma/Council-Time-Capsule.git>
cd COUNCIL_TIME_CAPSULE
pip install -r requirements.txt
python time_capsule(project-1).py

pip install -r requirements.txt

---
## Sample Usage
**Add Message with Image**

Welcome to Council Time Capsule!

Enter your name and surname: Orkun Bayraktar

1. Add message
Choose: 1

Hello, Orkun Bayraktar! Please write a message to future you:

Enter your message: See you in 2026!

Do you want to attach an image (yes/no): yes
Enter the path to the image file: ./photo.jpg
→ Image attached: capsule_images/image_20251103143025.jpg

Current date and time: 2025-11-03 14:30
Enter date and time (YYYY MM DD HH MM): 2026 01 01 00 00

Your message is saved until: 2026-01-01 00:00:00
Message sealed in time capsule!

```txt
2026-01-01 00:00|See you in 2026!|capsule_images/image_20251103143025.jpg

**View Unlocked**

Hello, Orkun Bayraktar! Here are your unlocked messages:

Unlocked Messages:

1. See you in 2026! (image: capsule_images/image_20251103143025.jpg)

**requirements.txt**

Pillow>=9.0.0

**Git Commands**

git add .
git commit -m "Final: Council Time Capsule with full datetime, Pillow, file structure"
git push origin main

git push
git add time_capsule.py requirements.txt README.md
git commit -m "Fix filename + final A+ README"
git push

# 🏎️ Asphalt Unite Legends AutoBot

> 🎮 A fun automation project using Python to grind tokens & complete quests in **Asphalt Unite Legends** — because sometimes grinding is boring, but getting blueprints isn't optional 😎

---

## 🔧 Features

- ✅ Starts the race automatically
- 🖱️ Detects and clicks tokens (no matter where they appear)
- 🎯 Uses multiple token images for accurate matching
- 🎮 Moves car with arrow keys and auto-drifts using SPACE
- 🔁 Finishes race and loops until you run out of tickets
- ✨ Runs with "vibe coding" energy

---

## 🧠 How It Works

- `1.py`: Collects tokens mid-race using image detection and keyboard movement
- `2.py`: Starts races, handles boost & finish screen, and auto-restarts loop

---

## 📁 Folder Structure

Asphalt-Unite-Legends-AutoBot/
├── .venv/
├── 1.py                              # In-race token detection + movement
├── 2.py                              # Race start/finish logic
├── Car Selection Button.png
├── Miss Out  button.png
├── Next Button white colour.png
├── Next Button Yellow  colour copy.png
├── Next Button Yellow  colour.png
├── Play button.png
├── Race-button.png
├── Screenshot 2025-07-04 013103-photoaidcom-cropped.png
├── Screenshot 2025-07-04 115418-modified.png
├── Screenshot 2025-07-04 115427-modified.png
├── Screenshot 2025-07-04 115455-modified.png
├── Screenshot 2025-07-04 115544-modified.png
├── Screenshot 2025-07-04 115629-modified.png
├── README.md

### 1. Install Requirements

```bash
pip install pyautogui keyboard opencv-python
```
## 2. Run the Scripts
In two separate terminals (or tabs):

```bash
python 2.py   # Starts & finishes race automatically
python 1.py   # Detects & collects tokens
```
## 3. Stop the Bot
Press ESC at any time to stop both scripts safely.

## ⏱️ Automation Loop
2.py:

Starts race → presses boost → finishes race → loops

1.py:

Continuously checks screen → detects any token image

Moves left or right based on position → collects token

## 🎮 Game Supported
Asphalt Unite Legends

No file editing or modding

Purely screen-based automation

Safe if used personally and responsibly

## 📌 Notes
Keep all .png images in the same folder as your Python scripts.

Add more token image versions if detection fails on some maps.

No folders needed for assets – just drop everything in the main folder.

.

## 🔥 Why I Made This?
“Sometimes grinding gets boring — but we need those blueprints!”

Just wanted to automate the boring parts of Asphalt 9 while still feeling like I’m making progress. Plus, it was a fun Python automation challenge. Sharing it here for fellow fans and coders

## ⚠️ Disclaimer
🧪 This tool is for educational and entertainment purposes only

🚫 Do not use in multiplayer or competitive modes

💀 Use at your own risk


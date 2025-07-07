import pyautogui
import time
import os
import random

# === CONFIGURATION ===
BUTTON_IMAGES = [
    "Race-button.png",
    "Car Selection Buttom .png",
    "Play button .png",
    "Next Button Yellow  colour.png",
    "Next Button Yellow  colour copy.png",
    "Miss Out  button.png",    
    "Next Button white colour.png"
  
]

CONFIDENCE = 0.8
SCAN_DELAY = 0.5  # Time between checks when image not found
COOLDOWN = 3     # Seconds to wait before clicking the same image again

print("[BOT] Running ordered button clicker with cooldown. Press Ctrl+C to stop.")

last_click_times = {img: 0 for img in BUTTON_IMAGES}  # Track last clicked time for each image

try:
    while True:
        for img_path in BUTTON_IMAGES:
            if not os.path.exists(img_path):
                print(f"[WARN] Image not found on disk: {img_path}")
                continue

            found = False
            while not found:
                try:
                    location = pyautogui.locateCenterOnScreen(img_path, confidence=CONFIDENCE)
                    if location:
                        now = time.time()
                        time_since_last_click = now - last_click_times[img_path]
                        if time_since_last_click < COOLDOWN:
                            # Skip clicking now, but keep scanning
                            print(f"[BOT] Waiting cooldown for '{img_path}' ({COOLDOWN - time_since_last_click:.1f}s left)")
                            time.sleep(SCAN_DELAY)
                            continue

                        # Click and update last clicked time
                        pyautogui.click(location)
                        print(f"[BOT] ✅ Clicked '{img_path}' at {location}")
                        last_click_times[img_path] = now
                        time.sleep(random.uniform(3, 4))  # Random delay between clicks
                        found = True
                    else:
                        time.sleep(SCAN_DELAY)
                except pyautogui.ImageNotFoundException:
                    print(f"[BOT] ⏳ Waiting for '{img_path}' (exception caught)...")
                    time.sleep(SCAN_DELAY)
        time.sleep(0.5)  # Optional pause after finishing one loop

except KeyboardInterrupt:
    print("\n[BOT] ❌ Stopped by user.")

import pyautogui
import time
import keyboard
import os

# === CONFIGURATION ===

TOKEN_IMAGES = [
    "Screenshot 2025-07-04 011853.png",
    "Screenshot 2025-07-04 115418-modified.png",
    "Screenshot 2025-07-04 013103-photoaidcom-cropped.png",
    "Screenshot 2025-07-04 115455-modified.png",
    "Screenshot 2025-07-04 115544-modified.png",
]

CONFIDENCE_LEVEL = 0.75
CLICK_DELAY = 2       # Wait 2 seconds after clicking (instead of separate wait and scan delay)
SCAN_DELAY = 0.05
SPACEBAR_INTERVAL = 10

# === INITIAL SETUP ===

last_space_press = time.time()
screen_width, _ = pyautogui.size()
last_detected_image = None
last_detect_time = 0

print("[BOT] Continuous token detection bot running. Press ESC to stop.")

# Check images exist once before starting loop
valid_images = [img for img in TOKEN_IMAGES if os.path.exists(img)]
missing = set(TOKEN_IMAGES) - set(valid_images)
for miss in missing:
    print(f"[WARN] Image not found (skipped): {miss}")

try:
    while True:
        if keyboard.is_pressed("esc"):
            print("[BOT] Stopped by user.")
            break

        now = time.time()

        # Press spacebar every SPACEBAR_INTERVAL seconds
        if now - last_space_press >= SPACEBAR_INTERVAL:
            keyboard.press_and_release("space")
            print("[BOT] → Pressed SPACEBAR.")
            last_space_press = now

        # Skip scanning if we just detected an image in last 2 seconds (waiting)
        if now - last_detect_time < CLICK_DELAY:
            time.sleep(SCAN_DELAY)
            continue

        detected = False
        for img_path in valid_images:
            try:
                location = pyautogui.locateCenterOnScreen(img_path, confidence=CONFIDENCE_LEVEL)
                if location:
                    # Avoid repeating same image immediately
                    if img_path == last_detected_image:
                        print(f"[BOT] Skipping repeated detection of {img_path}")
                        detected = True
                        break

                    direction = "left" if location.x < screen_width / 2 else "right"
                    keyboard.press_and_release(direction)
                    pyautogui.click(location)
                    print(f"[BOT] Detected token ({img_path}) → Pressed {direction.upper()}, Clicked at {location}")

                    last_detected_image = img_path
                    last_detect_time = now
                    detected = True
                    break
            except pyautogui.ImageNotFoundException:
                # No image found on screen, continue scanning others
                pass

        if not detected:
            last_detected_image = None  # Reset if no image found

        time.sleep(SCAN_DELAY)

except KeyboardInterrupt:
    print("\n[BOT] Exited by user.")
 
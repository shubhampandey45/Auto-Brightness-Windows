import time
import mss
import numpy as np
import screen_brightness_control as sbc
import keyboard
from PIL import Image
from plyer import notification  

# CONFIG
SAMPLE_FPS = 0.5  # every 2 seconds one snapshot
DOWNSAMPLE = (320, 180)
MIN_BRIGHT = 20
MAX_BRIGHT = 90
SMOOTH_ALPHA = 0.2
REGION_MODE = 'full'

stop_flag = False

def stop_program():
    global stop_flag
    stop_flag = True

keyboard.add_hotkey("ctrl+alt+b", stop_program)

def luminance_from_img(img):
    rgb = np.asarray(img, dtype=np.float32)
    Y = 0.2126*rgb[...,0] + 0.7152*rgb[...,1] + 0.0722*rgb[...,2]
    return float(Y.mean())

def map_luminance_to_brightness(Y):
    t = 1.0 - (Y / 255.0)
    t = t ** 0.9
    b = MIN_BRIGHT + t * (MAX_BRIGHT - MIN_BRIGHT)
    return int(round(b))

def show_notification(title, message, duration=4):
    # plyer notifications
    notification.notify(
        title=title,
        message=message,
        timeout=duration
    )

def main():
    global stop_flag
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        prev_b = sbc.get_brightness(display=0)[0] if sbc.list_monitors() else 50
        smoothed_b = prev_b
        interval = 1.0 / SAMPLE_FPS

        print("AutoBrightness started. Press CTRL+ALT+B to stop.")
        show_notification("AutoBrightness", "Started (CTRL+ALT+B to stop)", duration=4)

        try:
            while not stop_flag:
                start = time.time()
                bbox = {'left': monitor['left'], 'top': monitor['top'],
                        'width': monitor['width'], 'height': monitor['height']}
                raw = sct.grab(bbox)

                img = np.array(raw)[:,:,:3]
                pil = Image.fromarray(img[...,::-1])
                pil = pil.resize(DOWNSAMPLE, Image.BILINEAR)

                if REGION_MODE == 'split':
                    w2 = DOWNSAMPLE[0]//2
                    left = pil.crop((0,0,w2,DOWNSAMPLE[1]))
                    right = pil.crop((w2,0,DOWNSAMPLE[0],DOWNSAMPLE[1]))
                    Y = (luminance_from_img(left) + luminance_from_img(right)) / 2.0
                else:
                    Y = luminance_from_img(pil)

                target_b = map_luminance_to_brightness(Y)
                smoothed_b = (SMOOTH_ALPHA * target_b) + (1 - SMOOTH_ALPHA) * smoothed_b
                out_b = int(round(smoothed_b))

                if out_b != prev_b:
                    try:
                        sbc.set_brightness(out_b)
                        prev_b = out_b
                    except Exception as e:
                        print("Failed to set brightness:", e)

                elapsed = time.time() - start
                time.sleep(max(0, interval - elapsed))

        finally:
            show_notification("AutoBrightness", "Stopped", duration=4)
            print("Stopped.")

if __name__ == '__main__':
    main()
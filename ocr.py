import argparse
import cv2
import numpy as np
from PIL import ImageGrab, Image
import time
import pytesseract
import re
import pyautogui

def read_screen(screen_bbox, threshold, margin, process_every_n_frames=1, debug=False):
    frame_count = 0
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    initial_mouse_x, initial_mouse_y = x, y
    pyautogui.moveTo(initial_mouse_x, initial_mouse_y)

    def lag():
        print("Lag detected")
        pyautogui.mouseDown()
        pyautogui.move(-1, 0)
        pyautogui.mouseUp()

    def smooth():
        print("Running smoothly")

    def fast():
        print("Running fast")
        pyautogui.mouseDown()
        pyautogui.move(1, 0)
        pyautogui.mouseUp()

    while True:
        screenshot = ImageGrab.grab(bbox=screen_bbox)
        frame = np.array(screenshot)

        if frame_count % process_every_n_frames == 0:
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(frame_gray)

            speed_match = re.search(r'(x)(\d+)(\.\d{1,2})?', text)
            fps_match = re.search(r'(FPS\s*:\s*)(\d+)', text)

            if speed_match and fps_match:
                speed = float(speed_match.group(2) + (speed_match.group(3) or '.0'))
                fps = int(fps_match.group(2))

                if debug:
                    print(f"Speed: {speed}, FPS: {fps}")

                ratio = fps / speed

                if ratio < threshold - margin:
                    lag()
                elif threshold - margin <= ratio <= threshold + margin:
                    smooth()
                else:
                    fast()

        cv2.imshow('Frame', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    args = parser.parse_args()

    screen_bbox = (left of box, top of box, right of box, bottom of box)
    threshold = 8
    margin = 1.5
    read_screen(screen_bbox, threshold, margin, debug=args.debug)

import cv2
import numpy as np
from PIL import ImageGrab, Image
import time
import pytesseract
import re
import pyautogui

def read_screen(screen_bbox, threshold, margin, process_every_n_frames=1): # Change "process_every_n_frames" for the program to run at a higher or slower checking speed
    frame_count = 0
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Set the Tesseract executable path

    initial_mouse_x, initial_mouse_y = x, y  # Set the desired initial mouse position
    pyautogui.moveTo(initial_mouse_x, initial_mouse_y)

    def lag():
        print("Lag detected")
        pyautogui.mouseDown()  # Press the left mouse button
        pyautogui.move(-1, 0)  # Move the mouse 2 pixels to the left
        pyautogui.mouseUp()  # Release the left mouse button

    def smooth():
        print("Running smoothly")
        # Do nothing

    def fast():
        print("Running fast")
        pyautogui.mouseDown()  # Press the left mouse button
        pyautogui.move(1, 0)  # Move the mouse 2 pixels to the right
        pyautogui.mouseUp()  # Release the left mouse button


    while True:
        screenshot = ImageGrab.grab(bbox=screen_bbox)
        frame = np.array(screenshot)

        if frame_count % process_every_n_frames == 0:
            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            text = pytesseract.image_to_string(frame_gray)

            speed_match = re.search(r'(x)(\d+(\.\d+)?)', text)
            fps_match = re.search(r'(FPS\s*:\s*)(\d+)', text)

            if speed_match and fps_match:
                speed = float(speed_match.group(2))
                fps = int(fps_match.group(2))
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
    screen_bbox = (left of box, top of box, right of box, bottom of box)  # Replace with the desired coordinates
    threshold = 10  # Replace with the desired number for the threshold
    margin = 2   # Replace with the desired margin
    read_screen(screen_bbox, threshold, margin)

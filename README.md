
# Bibite Autospeed

A program to automatically alter the simulation speed of the simulator Bibites within a set range of frames per tick.

## Demo

Demo set to mantain 10 frames per tick with margin set to 2

https://youtu.be/DqgDdp_kmjQ
## Installation And Usage
- Requires python 3.x 
- Requires Tesseract 

1. Download Python from the official website 

2. Download Tesseract https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-5.3.1.20230401.exe

3. Download or clone this repository then open it.

4. Run "pip install -r requirements.txt" inside the repo.

* If this does not work run these commands individually 

pip install pyautogui

pip install pytesseract

pip install pygetwindow

pip install opencv-python

5. Use Mpos.exe to figure out the coordinates of stats box (https://ibb.co/khnMcMn) and the 1x speed position of the speed slider (https://ibb.co/phpjC6P)

6. Configure software by changing the screen_bbox = (left of box, top of box, right of box, bottom of box) to the coordinates captured using Mpos.exe

Change "initial_mouse_x, initial_mouse_y = x, y" to the X and Y coordinates of 1x on the speed slider collected with Mpos.exe

(Optional)

Change threshold and margin to desired values (See FAQ for explenations.)

7. Run program by running "python ocr.py" in the repo.
## FAQ

#### What is a "tick"

A tick is simply a simulated second. So at 10x speed there are 10 ticks per real second.

#### What does the threshold mean and what should I set it too?

The threshold is the minimum allowed frames per tick (FPT). For example at 60fps 1x speed you are getting 60 fpt. The official wiki does not recommend speeds above 5x. 5x speed at 60 fps would mean a fpt of 12. So by setting your threshold at 12 the program will keep your game running at either 60 fps or at a speed where 12 fpt is maintained. 

#### What does margin mean and what should I set it too?

Margin is how close the actual fpt has to be to your set threshold. I would recommend a margin betwee 1-2. 1 Might be a little jittery whilst 2 might be too lax, so find what you deem best. Although more testing is required so feel free to try any value.

#### What does "Running fast", "Running Smoothly" and "Lag Detected" mean?
Running fast means that the software deems there is room to increase simulator speed, Running Smoothly will maintain simulator speed and Lag Detected will decrease simulator speed.

#### How do I quit the program?
The program will automatically quit if you pause your simulation

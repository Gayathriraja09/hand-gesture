Features
	Cursor Movement: Move the index finger to control the cursor.
	Left Click: Pinch the thumb and index finger together.
	Right Click: Pinch the thumb and middle finger together.
	Smooth Cursor Movement: Uses smoothening to ensure stable cursor control.
Requirements
	Python 3.6 or later
	Camera (webcam or built-in)
Python Packages
Install the following Python libraries:
	pip install opencv-python mediapipe pyautogui numpy
Install Dependencies: 
Run the following command to install all required Python libraries:
	pip install -r requirements.txt
Alternatively, you can manually install each package listed in the Requirements section.

Run the Program: 
Start the program with the following command:
	python gesture_virtual_mouse.py
Usage
	Tkinter GUI: A Tkinter window with "Start Virtual Mouse" and "Stop Virtual Mouse" buttons will appear.
	Start Virtual Mouse: Click "Start Virtual Mouse" to initiate the hand-tracking and virtual mouse control.
	Stop Virtual Mouse: Click "Stop Virtual Mouse" to stop the virtual mouse control.
	Alternatively, press the 'q' key in the OpenCV video window to exit the program.
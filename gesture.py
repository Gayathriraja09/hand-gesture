import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import tkinter as tk
import threading
import math
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

smoothening = 5
plocx, plocy = 0, 0
clocx, clocy = 0, 0
running = False 

def start_virtual_mouse():
    global running
    running = True
    threading.Thread(target=run_virtual_mouse).start()

def stop_virtual_mouse():
    global running
    running = False
    cap.release()
    cv2.destroyAllWindows()

def calculate_distance(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

def run_virtual_mouse():
    global plocx, plocy, clocx, clocy
    while running:
        _, frame = cap.read()
        if not _:
            break
        
        frame_height, frame_width, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks
        
        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand)
                landmarks = hand.landmark
                
                index_tip = landmarks[8]
                thumb_tip = landmarks[4]
                middle_tip = landmarks[12]  # Middle finger tip for right-click gesture
                
                
                ix, iy = int(index_tip.x * frame_width), int(index_tip.y * frame_height)
                tx, ty = int(thumb_tip.x * frame_width), int(thumb_tip.y * frame_height)
                mx, my = int(middle_tip.x * frame_width), int(middle_tip.y * frame_height)

                index_x = (screen_width / frame_width) * ix
                index_y = (screen_height / frame_height) * iy
                clocx = plocx + (index_x - plocx) / smoothening
                clocy = plocy + (index_y - plocy) / smoothening
                pyautogui.moveTo(clocx, clocy)
                plocx, plocy = clocx, clocy
                
                pinch_dist = calculate_distance(ix, iy, tx, ty)
                right_click_dist = calculate_distance(ix, iy, mx, my)

                if pinch_dist < 40:
                    pyautogui.click()
                    pyautogui.sleep(0.3)  

                
                elif right_click_dist < 40:  
                    pyautogui.click(button='right')
                    pyautogui.sleep(0.3)  

        cv2.imshow('Virtual Mouse', frame)
        if cv2.waitKey(1) == ord('q'):
            break

root = tk.Tk()
root.title("Gesture-Controlled Virtual Mouse")

start_button = tk.Button(root, text="Start Virtual Mouse", command=start_virtual_mouse)
start_button.pack(pady=10)
stop_button = tk.Button(root, text="Stop Virtual Mouse", command=stop_virtual_mouse)
stop_button.pack(pady=10)

root.mainloop()

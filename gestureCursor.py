import cv2
import mediapipe as mp
import pyautogui
from pyautogui import moveTo
from mediapipe.tasks.python.components.containers import landmark

cap = cv2.VideoCapture(1)

hand_detector = mp.solutions.hands.Hands()
drawing= mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y=0
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width,ret  = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for i, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if i == 8:
                    cv2.circle(img=frame,center=(x, y), radius=10, color=(0, 255, 255) )
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(x, y)
                if i == 4:
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    if abs (index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow ('gesture mouse', frame)
    cv2.waitKey(1)

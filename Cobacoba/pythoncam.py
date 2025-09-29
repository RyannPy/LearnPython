import cv2
import mediapipe as mp
from gtts import gTTS
import pygame
from io import BytesIO
import threading
import time

# ===================== TTS ENGINE  =====================
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)

def play_audio(text):
    """Play audio di background thread"""
    print(f"[THREAD SPEAK] Starting: {text}")
    try:
        tts = gTTS(text=text, lang='en')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        
   
        pygame.mixer.music.stop()
        pygame.mixer.music.load(mp3_fp)
        pygame.mixer.music.play()
     
    except Exception as e:
        print(f"[ERROR] Thread TTS failed: {e}")

def speak(text):
    """Start thread untuk non-blocking speak"""
    thread = threading.Thread(target=play_audio, args=(text,), daemon=True)
    thread.start()

# ===================== HAND DETECTION =====================
mpHands = mp.solutions.hands
hands = mpHands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# ===================== STATE CONTROL =====================
last_fingers = -1
current_phrase = ""
last_speak_time = 0  
min_speak_interval = 0.8 

debounce_buffer = []
debounce_frames = 5

def count_fingers(hand_landmarks, handedness="Right"):
    finger_tips = [8, 12, 16, 20]
    finger_pip = [6, 10, 14, 18]
    fingers = []

    if handedness == "Right":
        fingers.append(1 if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x else 0)
    else:
        fingers.append(1 if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x else 0)

    for tip, pip in zip(finger_tips, finger_pip):
        fingers.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y else 0)

    return sum(fingers)

# ===================== MAIN LOOP =====================
while True:
    success, img = cap.read()
    if not success:
        break
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    fingers_up = None
    if results.multi_hand_landmarks and results.multi_handedness:
        if len(results.multi_hand_landmarks) >= 1:
            handLms = results.multi_hand_landmarks[0]
            hand_handedness = results.multi_handedness[0]
            label = hand_handedness.classification[0].label
            fingers_up = count_fingers(handLms, label)

            cv2.putText(img, f"Fingers: {fingers_up} ({label})", (10, 70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    if fingers_up is None:
        debounce_buffer.clear()
        current_phrase = ""
        last_fingers = -1
    else:
        debounce_buffer.append(fingers_up)
        if len(debounce_buffer) > debounce_frames:
            debounce_buffer.pop(0)

    if len(debounce_buffer) == debounce_frames and all(f == debounce_buffer[0] for f in debounce_buffer):
        stable_fingers = debounce_buffer[0]

        if stable_fingers == 5:
            current_phrase = "Hello"
        elif stable_fingers == 1:
            current_phrase = "My name is"
        elif stable_fingers == 2:
            current_phrase = "Ryan"
        else:
            current_phrase = ""
            last_fingers = -1

        if current_phrase:
            cv2.putText(img, current_phrase, (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        
        current_time = time.time()
        if current_phrase and stable_fingers != last_fingers and (current_time - last_speak_time > min_speak_interval):
            speak(current_phrase)
            last_speak_time = current_time
            last_fingers = stable_fingers

    cv2.imshow("Hand Gestures", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
hands.close()
pygame.mixer.quit()

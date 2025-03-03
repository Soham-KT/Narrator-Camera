import cv2
import time
import base64
import threading
from llm_api import FrameAPI, PersonalityAPI
from text_to_speech import tts_llm

cap = cv2.VideoCapture(0)
frame = None
lock = threading.Lock()
image_api = FrameAPI()
personality_api = PersonalityAPI()

def send_frame():
    global frame
    while True:
        time.sleep(5)  # Wait for 5 seconds
        with lock:
            if frame is not None:
                encoded_frame = base64.b64encode(cv2.imencode('.jpeg', frame)[1]).decode()
        description = image_api.get_image_description(encoded_frame)

        new_description = personality_api.get_personality_description(description)
        print(new_description)
        tts_llm(new_description)

# Start the API thread
threading.Thread(target=send_frame, daemon=True).start()

while True:
    ret, new_frame = cap.read()
    if not ret:
        break

    with lock:
        frame = new_frame.copy()

    cv2.imshow('webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
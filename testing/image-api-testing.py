import cv2
from openai import OpenAI
import base64

def encode_frame(frame):
    _, buffer = cv2.imencode('.jpeg', frame)
    return base64.b64encode(buffer).decode('utf-8')

cap = cv2.VideoCapture(0)

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

ret, frame = cap.read()
if not ret:
    print('could not read frame')
    exit()

encoded_frame = encode_frame(frame)

response = client.chat.completions.create(
    model="llava-v1.5-7b",
    messages=[
        {"role": "system", "content": "keep it under 50 words"},
        {"role": "user",
         "content": [
             {
                 'type' : 'text',
                 'text' : 'What is in the image?'
             },
             {
                 'type' : 'image',
                 'image_url' : {
                     'url' : f'data:image/jpeg;base64,{encoded_frame}'
                 }
             } 
         ]}
    ],
    temperature=0.7,
)

print(response.choices[0].message.content)
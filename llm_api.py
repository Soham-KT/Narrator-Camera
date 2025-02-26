from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio") 


# Class to get image description
class FrameAPI:
    def __init__(self):
        self.client = client
    
    def get_image_description(self, encoded_frame, temperature = 0.7):
        completion = self.client.chat.completions.create(
            model='llava-v1.5-7b',
            messages=[
                {"role": "system", "content": "talk like deadpool and keep it under 50 words"},
                {"role": "user",
                 "content": [
                     {
                         'type' : 'text',
                         'text' : 'Describe this image'
                     },
                     {
                         'type' : 'image',
                            'image_url' : {
                                'url' : f'data:image/jpeg;base64,{encoded_frame}'
                            }
                     }
                 ]}
            ],
            temperature=temperature,
        )
        return completion.choices[0].message.content
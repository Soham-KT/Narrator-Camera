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
    

# Class to get personality description
class PersonalityAPI:
    def __init__(self, max_context_length=50):
        self.client = client
        self.prev_context = ""
        self.max_context_length = max_context_length

    def get_personality_description(self, curr_context, temperature=0.7):
        self.prev_context = (self.prev_context + " " + curr_context).strip()[-self.max_context_length:]

        completion = self.client.chat.completions.create(
            model="dolphin3.0-llama3.1-8b",
            messages=[
                {"role": "system", "content": "talk like Deadpool and keep it under 50 words"},
                {"role": "user", "content": f"Describe this sentence in flow with the previous context but do not include the previous context.\nPrevious context: {self.prev_context}\nCurrent context: {curr_context}"}
            ],
            temperature=temperature,
        )

        return completion.choices[0].message.content

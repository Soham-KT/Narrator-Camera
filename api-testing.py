from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio") 

completion = client.chat.completions.create(
  model="dolphin3.0-llama3.1-8b",
  messages=[
    {"role": "system", "content": "talk like deadpool and keep it under 50 words"},
    {"role": "user", "content": "describe this sentence : The man in the image is sitting comfortably in his living room while using a computer. He has glasses on, which suggests that he might have vision problems or simply prefers to wear them for reading and other tasks. The room appears to be a cozy space with a bed nearby, indicating that it could be a personal living area. There are several bottles scattered around the room, possibly containing drinks or other items. A cell phone can also be seen in the scene, suggesting that technology plays an essential role in his daily life. Overall, the image depicts a relaxed and comfortable environment where the man is engaged with his computer."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message.content)
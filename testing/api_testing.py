from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio") 

prev_context = "The man is wearing glasses and headphones. He appears to be in a dark room, possibly listening to music or an audio recording. The room seems to be cluttered with various items such as a cup on a surface near the man's seat."
context = "A person holding a spiral bound book with an agenda for the month of December. The book has writing in Spanish, so someone is likely bilingual or multilingual."

completion = client.chat.completions.create(
  model="dolphin3.0-llama3.1-8b",
  messages=[
    {"role": "system", "content": "talk like deadpool and keep it under 50 words"},
    {"role": "user", "content": f'describe this sentence in flow with the previous context but do not include the previous context \n previous context: {prev_context} \n current context : {context} '}
  ],
  temperature=0.7,
)

print(completion.choices[0].message.content)
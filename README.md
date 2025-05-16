# Narrator-Camera: Real-Time Personality-Powered Webcam Narrator 🕶️🎤

Narrator-Camera or NarrateCam is a real-time computer vision project that captures webcam footage, uses a large language model (LLM) to generate funny Deadpool-style (or any personality of choice) descriptions of the scene, enhances them with a personality-aware context engine, and finally speaks them out loud using text-to-speech.

## 🔧 Features

* 📸 Captures live video feed from webcam
* 🧠 Describes frames using an image LLM (LLaVA)
* 🗣️ Adds contextual, personality-driven humor (Deadpool-style)
* 🔊 Speaks the description using text-to-speech (TTS)

## 🗂️ Project Structure

```
.
├── main.py               # Core script to capture webcam, send frames, display, and speak
├── llm_api.py            # Handles interaction with image and text LLMs
└── text_to_speech.py     # Converts generated text to speech using pyttsx3
```

## 🛠️ Requirements

* Python 3.8+
* OpenCV
* pyttsx3
* OpenAI-compatible LLM server (like LM Studio)
* Local LLaVA (`llava-v1.5-7b`) and Dolphin (`dolphin3.0-llama3.1-8b`) models running via `http://localhost:1234/v1`

### Install dependencies

```bash
pip install opencv-python pyttsx3 openai
```

## 🚀 Getting Started

1. **Run your LLMs**:
   Launch your LLaVA and Dolphin models using LM Studio or another OpenAI-compatible server on `localhost:1234`.

2. **Start the app**:
   Run the main script:

   ```bash
   python main.py
   ```

3. **See it in action**:

   * A webcam window opens
   * Every 5 seconds, the current frame is described in Deadpool-style humor
   * The description is read aloud using TTS
   * Press `q` to quit

## 🧠 How It Works

1. `main.py` captures frames from the webcam.
2. Every 5 seconds, the current frame is base64-encoded and sent to the image model (`llava-v1.5-7b`) for visual description.
3. That description is passed into a contextual personality engine (`dolphin3.0-llama3.1-8b`) that keeps a brief context history.
4. The final personalized message is spoken aloud using `pyttsx3`.

## 🗣 Example Output

```
🎥 Scene: "A guy sitting in front of a laptop with a look of existential dread. Classic."
🧠 Contextual Deadpool-style message: "Oh, the face of someone trying to debug on a Friday night. Bravo!"
🔊 Spoken via TTS.
```

## 📌 Notes

* Make sure LM Studio or the API server is running with the correct models.
* If audio playback fails, check that your system supports `pyttsx3` (Windows and macOS generally work out of the box).

## 📄 License

MIT License

---

Let me know if you'd like a version with emojis removed or formatted for a different style (e.g., professional documentation).

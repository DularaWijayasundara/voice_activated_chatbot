**Voice-Activated Chatbot**

This project implements a voice-activated chatbot using OpenAI's GPT-3.5 model. The chatbot listens to user input via the microphone, processes it using speech recognition, generates responses using GPT-3.5, and vocalizes the answers.

**Setup:**

1. **Install the required dependencies:**
   - `pyttsx3`
   - `speech_recognition`
   - `OpenAI`

2. **Obtain an API key from OpenAI:**
  

3. **Save your OpenAI API key:**
   - Create a separate Python file named `creds.py`.
   - Save your API key in `creds.py` using the format: `api_key = "YOUR_API_KEY"`.

**Usage:**

- Execute the script in your Python environment.
- The script will continuously listen for voice input from the microphone.
- Speak into the microphone to ask questions, give commands, or engage in conversation.
- The chatbot will process your spoken input, generate responses using the GPT-3.5 model, and vocalize the answers using text-to-speech.
- To exit the chatbot, simply say "quit", "exit", or "bye".

import pyttsx3
import speech_recognition
from openai import OpenAI
import creds

textspeech = pyttsx3.init()

recognizer = speech_recognition.Recognizer()

client = OpenAI(
    api_key=creds.api_key
)

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    try:
        print("Speak something...")
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.3)
            audio = recognizer.listen(mic)

            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(str(text))

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        print("Sorry, could not understand audio.")
        continue
    except speech_recognition.RequestError as e:
        print("Could not request results; {0}".format(e))


    message = text
    if message.lower() in ["quit", "exit", "bye"]:
       break
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat_completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  messages=messages
        )

    reply = chat_completion.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
    textspeech.say(str(reply))
    textspeech.runAndWait()

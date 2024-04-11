import pyttsx3
from openai import OpenAI
import creds

textspeech = pyttsx3.init()

client = OpenAI(
    api_key=creds.api_key
)

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

while True:
    message = input("User : ")
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


# The following works on googlecolab
# !pip install gTTS

# from gtts import gTTS
# import IPython.display as ipd

# tts = gTTS("Hello World")
# tts.save("hello.mp3")

# # Play the generated audio
# ipd.Audio('hello.mp3', autoplay=True)

